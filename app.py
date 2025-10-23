# ...existing code...
import streamlit as st
from PIL import Image

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] > .main, .block-container {
        background-color: #BFE6FF;
    }
    * {
        color: #000000 !important;
        font-family: 'Montserrat', sans-serif !important;
    }
    .stButton>button, input, textarea, select, .stTextInput, .stSelectbox, .stRadio, .stCheckbox {
        color: #000000 !important;
        font-family: 'Montserrat', sans-serif !important;
    }
    .stImage figure figcaption, .stCaption {
        color: #000000 !important;
        font-family: 'Montserrat', sans-serif !important;
    }
    [data-testid="stSidebar"] {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(" Mi Primera App!!")

st.header("Aquí inicio la creación y prueba de interfaces multimodales para mis aplicaciones.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("imagen 2.webp")

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
# ...existing code...
