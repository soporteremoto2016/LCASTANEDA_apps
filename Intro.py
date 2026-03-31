import streamlit as st
from PIL import Image
# Aplicar CSS solo a la Sidebar
st.markdown(
    """
    <style>
    /* 1. Fondo azul para la barra lateral */
    section[data-testid="stSidebar"] {
        background-color: blue !important;
    }

    /* 2. Color blanco0 para todos los textos dentro de la barra lateral */
    section[data-testid="stSidebar"] .stText, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: white !important;
    }

    /* 3. Opcional: Cambiar el color de los iconos de cerrar/abrir de la sidebar */
    section[data-testid="stSidebar"] button svg {
        fill: #0000FF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tu contenido de la sidebar

with st.sidebar:
    st.subheader("Luis Castañeda")    
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "Herramientas desarrolladas para identificar la funcionalidad de la Inteligencia Artificial "
        "y dar ideas de como pueden ser aplicadas dentro de las organizaciones "
        "para permitir la facilidad y ejecución de procesos."
    )
         
    st.write(parrafo)

# Contenido principal (esto se mantendrá con los colores por defecto)
st.title("Apliaciones IA ")

#url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Pruebas de Concepto aplicadas a IA")
#st.write(f"Pruebas de Concepto aplicadas a IA : [Enlace]({url_ia})")
col1, col2, col3, col4 = st.columns(4)

with col1:
 
 st.subheader("Detección de Objetos")
 image = Image.open('Analisis_Imagenes.jpg')
 st.image(image, width=190)
 st.write("Sistema que permite identifcar con Video Objetos") 
 url = "https://yolov5-hpaetkatdrdpj4jkhy8qex.streamlit.app/"
 st.write(f"Objetos: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5cmc.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Analisis de Imagenes")
 image = Image.open('Clasificar.jpg')
 st.image(image, width=200)
 st.write("Es una aplicación que permite clasificar imagenes.") 
 url = "https://multimodalgptlc.streamlit.app/"
 st.write(f"Imagenes: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Clasificar Vehículos, Motos y Bicicletas ")
 image = Image.open('Clasificar_Motos.jpg')
 st.image(image, width=190)
 st.write("Sistema que clasifica imagens de Vehiculos, Motos y Bicicletas.") 
 url = "https:https://tmimglc.streamlit.app/"
 st.write(f"Movimiento: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 

with col4: 
 st.subheader("Clasificador de Flores")
 image = Image.open('Clasificar_Flores.jpg')
 st.image(image, width=190)
 st.write("Permite identificar una foto de una flor y clasificarla en un grupo especifico.") 
 url = "https://tlflores-lc.streamlit.app/"
 st.write(f"Flores: [Enlace]({url})")
 
 st.subheader("Clasificador de Flores")
 image = Image.open('Clasificar_Flores.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 #st.write(f"RAG: [Enlace]({url})")

 st.subheader("Clasificador de Flores")
 image = Image.open('Clasificar_Flores.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 #st.write(f"RAG: [Enlace]({url})")
 
 
