import streamlit as st
import random

def generar_ecuacion_lineal(dificultad):
    # Rango de números según dificultad
    limite = dificultad * 10
    a = random.randint(1, limite)
    b = random.randint(-limite, limite)
    x = random.randint(-limite, limite)
    
    # Calculamos c para que x sea siempre un entero (más amigable)
    c = a * x + b
    
    signo = "+" if b >= 0 else ""
    ecuacion_latex = f"{a}x {signo} {b} = {c}"
    return ecuacion_latex, x

def generar_ecuacion_cuadratica(dificultad):
    # (x - r1)(x - r2) = 0  => x^2 - (r1+r2)x + (r1*r2) = 0
    limite = dificultad * 5
    r1 = random.randint(-limite, limite)
    r2 = random.randint(-limite, limite)
    
    b = -(r1 + r2)
    c = r1 * r2
    
    signo_b = "+" if b >= 0 else ""
    signo_c = "+" if c >= 0 else ""
    
    ecuacion_latex = f"x^2 {signo_b} {b}x {signo_c} {c} = 0"
    return ecuacion_latex, (min(r1, r2), max(r1, r2))

# --- Configuración de la Interfaz ---
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="🧮")
st.title("🧮 Generador de Ecuaciones Pro")
st.markdown("Pon a prueba tus habilidades matemáticas o genera ejercicios.")

with st.sidebar:
    st.header("Configuración")
    tipo = st.selectbox("Tipo de ecuación", ["Lineal", "Cuadrática"])
    nivel = st.slider("Nivel de dificultad", 1, 10, 1)
    if st.button("Generar nueva ecuación"):
        st.rerun()

# --- Lógica de Generación ---
if tipo == "Lineal":
    ec, sol = generar_ecuacion_lineal(nivel)
    st.info("Resuelve para $x$:")
    st.latex(ec)
else:
    ec, sol = generar_ecuacion_cuadratica(nivel)
    st.info("Encuentra las raíces de:")
    st.latex(ec)

# --- Sección de Respuesta ---
with st.expander("Ver solución"):
    if tipo == "Lineal":
        st.write(f"La respuesta es: **x = {sol}**")
    else:
        st.write(f"Las raíces son: **x₁ = {sol[0]}** y **x₂ = {sol[1]}**")

# Estética extra
st.divider()
st.caption("Generado con Python y Streamlit")
