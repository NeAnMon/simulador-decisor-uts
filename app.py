import streamlit as st

# Configuración de la página
st.set_page_config(page_title="El Decisor - UTS", page_icon="🤖")

st.title("🤖 Simulador: El Decisor")
st.markdown("""
Esta herramienta te ayuda a entender cómo los **Condicionales Anidados** permiten que un programa tome decisiones complejas.
""")

st.divider()

# Sección de Entrada de Datos
st.subheader("1. Entrada de Datos (Variables)")
nombre = st.text_input("Ingresa tu nombre:", "Estudiante")
carnet = st.radio(f"¿{nombre}, tienes tu carnet físico o digital?", ("Sí", "No"))

# Lógica del Decisor (Condicionales Anidados)
if carnet == "Sí":
    st.info("Primer condicional superado: `if carnet == 'Sí':`")
    
    horario = st.radio("¿Es horario de clase actualmente?", ("Sí", "No"))
    
    if horario == "Sí":
        # Condicional Anidado
        st.success(f"✅ ¡Acceso Concedido! Bienvenido al Lab, {nombre}.")
        st.balloons()
    else:
        st.warning(f"⚠️ {nombre}, acceso denegado. Solo se permite ingreso en horario académico.")
else:
    st.error("❌ Acceso Denegado. Por favor, dirígete a Bienestar Universitario por tu carnet.")

st.divider()

# Sección de Abstracción para el estudiante
with st.expander("Ver la Lógica Detrás (Código Python)"):
    st.code(f'''
if carnet == "Sí":
    if horario == "Sí":
        print("Acceso Concedido")
    else:
        print("Acceso denegado por horario")
else:
    print("Acceso denegado por falta de carnet")
    ''')