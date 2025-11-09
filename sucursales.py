import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
import os

# --- Configuración inicial ---
EXCEL_PATH = "registros.xlsx"
jornadas = {1: "Mañana", 2: "Tarde", 3: "Noche"}
precios = {1: 0.83, 2: 0.88, 3: 0.92}
litros_a_galones = lambda l: l / 3.785

#Cargar o inicializar Excel
if "df_excel" not in st.session_state:
    if os.path.exists(EXCEL_PATH):
        st.session_state.df_excel = pd.read_excel(EXCEL_PATH)
    else:
        st.session_state.df_excel = pd.DataFrame(columns=["Sucursal", "Servicio", "Jornada", "Monto $", "Litros"])

#Interfaz principal - Registro de servicios
st.title("⛽ Registro de Servicios de Gasolina")

modo = st.radio("Modo de uso", ["Registrar nuevo servicio", "Solo ver resumen desde Excel"])

if modo == "Registrar nuevo servicio":
    with st.form("registro"):
        sucursal = st.selectbox("Sucursal", ["Sucursal 1", "Sucursal 2"])
        servicio = st.selectbox("Servicio", ["Diesel", "Gasolina91", "Gasolina95"])
        jornada = st.selectbox("Jornada", list(jornadas.values()))
        monto = st.number_input("Monto vendido ($)", min_value=0.0, step=0.01, key="monto_input")
        enviar = st.form_submit_button("Registrar")

        if enviar and monto > 0:
            precio = precios[[1, 2, 3][["Diesel", "Gasolina91", "Gasolina95"].index(servicio)]]
            litros = monto / precio
            nuevo = pd.DataFrame([{
                "Sucursal": sucursal,
                "Servicio": servicio,
                "Jornada": jornada,
                "Monto $": monto,
                "Litros": litros
            }])
            st.session_state.df_excel = pd.concat([st.session_state.df_excel, nuevo], ignore_index=True)
            st.session_state.df_excel.to_excel(EXCEL_PATH, index=False)
            st.success("✅ Registro guardado correctamente")
            st.session_state["monto_input"] = 0.0  #limpia el campo

#Mostrar resumen
df = st.session_state.df_excel.copy()
if df.empty:
    st.info("No hay datos registrados aún.")
else:
    st.markdown("## 📋 Reporte del Día")
    df["Galones"] = df["Litros"].apply(litros_a_galones)
    st.dataframe(df)

    st.markdown("### 💼 Totales por Sucursal y Servicio")
    totales = df.groupby(["Sucursal", "Servicio"])[["Monto $", "Litros", "Galones"]].sum().reset_index()
    st.dataframe(totales)

    st.markdown("### 🕒 Totales por Jornada")
    por_turno = df.groupby("Jornada")[["Monto $", "Litros"]].sum().reset_index()
    st.dataframe(por_turno)

    st.markdown("### 🏅 Mejor Turno y Servicio por Sucursal")
    for suc in df["Sucursal"].unique():
        st.markdown(f"**{suc}**")
        df_suc = df[df["Sucursal"] == suc]
        mejor_turno = df_suc.groupby("Jornada")["Monto $"].sum().idxmax()
        mejor_servicio = df_suc.groupby("Servicio")["Monto $"].sum().idxmax()
        st.write(f"- Mejor turno: {mejor_turno}")
        st.write(f"- Mejor servicio: {mejor_servicio}")

    st.markdown("### ⚖️ Comparativa entre Sucursales por Servicio")
    for serv in df["Servicio"].unique():
        df_serv = df[df["Servicio"] == serv]
        mejor_suc = df_serv.groupby("Sucursal")["Monto $"].sum().idxmax()
        st.write(f"- {serv}: mayor venta en **{mejor_suc}**")

    st.markdown("### 🥧 Gráfico de pastel por servicio")
    ventas_por_servicio = df.groupby("Servicio")["Monto $"].sum()
    labels = ventas_por_servicio.index.tolist()
    sizes = ventas_por_servicio.values.tolist()
    total = sum(sizes)

    def etiqueta(pct):
        valor = pct * total / 100
        return f"{pct:.1f}%\n${valor:.2f}"

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, autopct=etiqueta, startangle=90, counterclock=False, wedgeprops={'edgecolor': 'white'})
    ax.set_title("Distribución de Ventas por Servicio", fontsize=14)
    ax.axis('equal')
    st.pyplot(fig)

    st.markdown("### 📄 Exportar resumen a PDF")
    def generar_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="Resumen del día - Gasolineras", ln=True, align="C")
        pdf.set_font("Arial", "I", 10)
        pdf.cell(200, 10, txt=f"Generado el: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align="C")
        pdf.ln(10)

        for suc in df["Sucursal"].unique():
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=suc, ln=True)
            pdf.set_font("Arial", size=11)
            df_suc = df[df["Sucursal"] == suc]
            for serv in df_suc["Servicio"].unique():
                total_monto = df_suc[df_suc["Servicio"] == serv]["Monto $"].sum()
                total_litros = df_suc[df_suc["Servicio"] == serv]["Litros"].sum()
                pdf.cell(200, 8, txt=f"- {serv}: ${total_monto:.2f}, {total_litros:.2f} L", ln=True)

        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="Comparativa por servicio", ln=True)
        pdf.set_font("Arial", size=11)
        for serv in df["Servicio"].unique():
            df_serv = df[df["Servicio"] == serv]
            mejor_suc = df_serv.groupby("Sucursal")["Monto $"].sum().idxmax()
            pdf.cell(200, 8, txt=f"{serv}: mayor venta en {mejor_suc}", ln=True)

        return bytes(pdf.output(dest="S"))

    if st.button("📥 Descargar PDF"):
        pdf_bytes = generar_pdf()
        st.download_button("Descargar reporte en PDF", data=pdf_bytes, file_name="reporte_gasolina.pdf", mime="application/pdf")