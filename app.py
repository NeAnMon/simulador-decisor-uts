import streamlit as st

# 1. Configuración de la página y Estética Tech
st.set_page_config(page_title="El Decisor - UTS", page_icon="🤖", layout="centered")

# Estilos personalizados corregidos
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #3498DB;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True) # <-- Aquí estaba el error, ya está corregido

# 2. Encabezado
st.title("🤖 Simulador: El Decisor")
st.markdown("""
Esta herramienta interactiva está diseñada para los estudiantes de las **UTS**. 
Aprenderás cómo los **Condicionales Anidados** permiten que un programa tome decisiones lógicas.
""")

st.divider()

# 3. Sección de Entrada de Datos (Variables)
st.subheader("1. Entrada de Datos (Variables)")
col1, col2 = st.columns(2)

with col1:
    nombre = st.text_input("Ingresa tu nombre:", "Estudiante")
with col2:
    carnet = st.radio(f"¿{nombre}, tienes tu carnet?", ("Sí", "No"))

# 4. Lógica del Decisor (Condicionales Anidados)
st.subheader("2. Proceso de Decisión")

if carnet == "Sí":
    st.info("✅ Primer condicional superado: `if carnet == 'Sí':`")
    
    horario = st.radio("¿Es horario de clase actualmente?", ("Sí", "No"))
    
    if horario == "Sí":
        # Condicional Anidado
        st.success(f"🎉 ¡Acceso Concedido! Bienvenido al Lab, {nombre}.")
        st.balloons()
    else:
        st.warning(f"⚠️ {nombre}, acceso denegado. Solo se permite ingreso en horario académico.")
else:
    st.error("❌ Acceso Denegado. Por favor, dirígete a Bienestar Universitario por tu carnet.")

# 5. Sección de Abstracción (Ver el código)
with st.expander("🔍 Ver la Lógica Detrás (Código Python)"):
    st.code(f'''
# Estructura lógica del simulador
if carnet == "Sí":
    if horario == "Sí":
        print("Acceso Concedido")
    else:
        print("Acceso denegado por horario")
else:
    print("Acceso denegado por falta de carnet")
    ''', language="python")

st.divider()

# 6. Laboratorio de Lógica (Interacción Directa)
st.subheader("🧪 Laboratorio de Lógica")
st.write("Escribe una condición y prueba cómo la evalúa Python en tiempo real:")

col3, col4 = st.columns([2, 1])

with col3:
    condicion_alumno = st.text_input("Tu lógica (ej: nota >= 3.0):", "nota >= 3.0")
with col4:
    valor_nota = st.number_input("Valor de 'nota':", 0.0, 5.0, 3.5, step=0.1)

# Evaluar la lógica del alumno dinámicamente
try:
    nota = valor_nota
    resultado = eval(condicion_alumno)
    
    if resultado:
        st.success(f"Resultado: **VERDADERO** (TRUE). El estudiante APRUEBA.")
    else:
        st.error(f"Resultado: **FALSO** (FALSE). El estudiante REPRUEBA.")
except Exception as e:
    st.warning("⚠️ Esperando una condición válida... (Usa variables y operadores como >, <, ==)")

st.divider()

# 7. Gamificación: Encuentra el Bug
st.subheader("🕵️ Desafío: Encuentra el Bug")
st.write("""
El siguiente código tiene un **error de lógica**. Aunque el estudiante tenga un **1.0**, el sistema dice que 'Aprobó'. 
**¿Puedes escribir la condición correcta en el cuadro de abajo?**
""")

st.code('''
# LÍNEA 15: Error de lógica
# Este código deja pasar a todos los que tengan más de 0
if nota > 0: 
    print("¡Aprobaste!")
''', language="python")

solucion_alumno = st.text_input("Escribe la condición corregida aquí:", "")

if solucion_alumno:
    # Validamos con una nota que debería fallar (1.5)
    try:
        nota_test = 1.5
        # Usamos un entorno controlado para evaluar la respuesta del alumno
        if eval(solucion_alumno, {"nota": 1.5}) == False and eval(solucion_alumno, {"nota" >= 3.0}) == True:
            st.success("✨ ¡Excelente! Has corregido el bug. Ahora el sistema solo aprueba con 3.0 o más.")
        else:
            st.error("❌ El bug sigue ahí. Tu lógica aún permite aprobar a alguien con 1.5.")
    except:
        st.info("Escribe una comparación válida, por ejemplo: nota >= 3.0")

st.caption("Recurso diseñado para las Unidades Tecnológicas de Santander - UTS")


