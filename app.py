import streamlit as st
import random
import sympy as sp

def generate_equation(eq_type):
    x = sp.symbols('x')
    
    if eq_type == "Lineal":
        # ax + b = c
        a, b, c = [random.randint(1, 10) for _ in range(3)]
        equation = sp.Eq(a*x + b, c)
        
    elif eq_type == "Cuadrática":
        # ax^2 + bx + c = 0
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        
    else: # Trigonométrica simple
        # sin(ax) = b/c
        a = random.randint(1, 4)
        equation = sp.Eq(sp.sin(a*x), sp.Rational(1, 2))

    return equation

# Configuración de la UI
st.title("MathGen: Generador de Ecuaciones")
st.sidebar.header("Configuración")

tipo = st.sidebar.selectbox("Tipo de ecuación", ["Lineal", "Cuadrática", "Trigonométrica"])

if st.button("Generar Nueva Ecuación"):
    eq = generate_equation(tipo)
    st.session_state.current_eq = eq
    st.session_state.solution = sp.solve(eq, sp.symbols('x'))

if 'current_eq' in st.session_state:
    st.write("### Ecuación:")
    # Renderizado en LaTeX
    st.latex(sp.latex(st.session_state.current_eq))
    
    if st.checkbox("Mostrar Solución"):
        st.write("### Solución:")
        for sol in st.session_state.solution:
            st.latex(f"x = {sp.latex(sol)}")
