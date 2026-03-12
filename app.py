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
    try:
        # Definimos los casos de prueba rigurosos
        casos = {
            "muy_bajo": 1.5,
            "casi_pasa": 2.99,  # Si el alumno usa nota > 2, este caso lo atrapa
            "aprobado": 3.0
        }

        # Evaluamos la lógica del alumno en los tres escenarios
        res_muy_bajo = eval(solucion_alumno, {"nota": casos["muy_bajo"]})
        res_casi_pasa = eval(solucion_alumno, {"nota": casos["casi_pasa"]})
        res_aprobado = eval(solucion_alumno, {"nota": casos["aprobado"]})

        # La condición para el ÉXITO es:
        # Debe ser Falso para 1.5 AND Falso para 2.99 AND Verdadero para 3.0
        if res_muy_bajo == False and res_casi_pasa == False and res_aprobado == True:
            st.success(f""✨ ¡Excelente! Has corregido el bug. Ahora el sistema es estricto y solo aprueba con 3.0 o más.")
            st.balloons()
        else:
            st.error("❌ El bug sigue ahí. Tu lógica todavía es muy permisiva y deja pasar notas menores a 3.0.")
            
            # Feedback pedagógico adicional
            if res_casi_pasa == True:
                st.warning("Pista: Alguien con 2.99 está aprobando con tu código. ¡Ajusta el operador!")
                
    except Exception as e:
        st.info("Escribe una comparación válida. Ejemplo: `nota >= 3.0`")

st.caption("Recurso diseñado para las Unidades Tecnológicas de Santander - UTS")





