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
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
 
 st.subheader("Detección de Objetos")
 image = Image.open('Analisis_Imagenes.jpg')
 st.image(image, width=190)
 st.write("Sistema que permite identifcar con Video Objetos") 
 url = "https://yolov5-hpaetkatdrdpj4jkhy8qex.streamlit.app/"
 st.write(f"Objetos: [Enlace]({url})")

 st.subheader("Análisis de Sentimientos")
 image = Image.open('Sentimientos.jpg')
 st.image(image, width=200)
 st.write("Identifica el contexto que se escribe y valida el sentimiento que tiene.") 
 url = "https://sentimientoslc.streamlit.app"
 st.write(f"Sentimiento: [Enlace]({url})")

 st.subheader("Diseño de Nubes de Palabras")
 image = Image.open('Nube.jpg')
 st.image(image, width=200)
 st.write("De un conjunto de Texto se analiza cada palabra , se correlaciona y crea Nubes de palabras.") 
 url = "https://wordcloud-nubelc.streamlit.app/"
 st.write(f"Nube: [Enlace]({url})")

with col2: 
 st.subheader("Análisis de Imágenes")
 image = Image.open('Clasificar.jpg')
 st.image(image, width=200)
 st.write("                                Es una aplicación que permite clasificar imagenes.              ") 
 url = "https://multimodalgptlc.streamlit.app/"
 st.write(f"Imagenes: [Enlace]({url})")

 st.subheader("Traductor (escucha a voz)")
 image = Image.open('Traductor.jpg')
 st.image(image, width=190)
 st.write("Permite traducir un mensaje en voz a otro idioma ademas de permitir escribirlo en texto .") 
 url = "https://traductor--textlc.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

 st.subheader("Chat Conversacional")
 image = Image.open('Chat.jpg')
 st.image(image, width=200)
 st.write("Permite tener una conversación con el chatbot sobre un tema en especifico.") 
 url = "https://chatbotopenailc.streamlit.app/"
 st.write(f"Chat: [Enlace]({url})")


with col3: 
 st.subheader("Clasificar Vehículos, Motos y Bicicletas ")
 image = Image.open('Clasificar_Motos.jpg')
 st.image(image, width=190)
 st.write("Sistema que clasifica imagens de Vehiculos, Motos y Bicicletas.") 
 url = "https:https://tmimglc.streamlit.app/"
 st.write(f"Movimiento: [Enlace]({url})")

 st.subheader("Convertir Texto a Audio")
 image = Image.open('Texto_Audio.jpg')
 st.image(image, width=200)
 st.write("Permite realizar conversión de un Texto a  audio.") 
 url = "https://speedtexttlc.streamlit.app/"
 st.write(f"Convertir Audio: [Enlace]({url})")
 
 st.subheader("Chat Anthropic")
 image = Image.open('Chat_Ant.jpg')
 st.image(image, width=200)
 st.write("Chat directamente con ML Anthropic.")
 url = "https://antchgptlc.streamlit.app"
 st.write(f"Convertir Audio: [Enlace]({url})")

with col4: 
 st.subheader("Clasificador de Flores")
 image = Image.open('Clasificar_Flores.jpg')
 st.image(image, width=190)
 st.write("Permite identificar una foto de una flor y clasificarla en un grupo especifico.") 
 url = "https://tlflores-lc.streamlit.app/"
 st.write(f"Flores: [Enlace]({url})")
 
 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('REC_OCR.jpg')
 st.image(image, width=190)
 st.write("Identifica la información en una imagen o de Video, la selecciona y la almacena en Texto  .") 
 url = "https://ocr-audiolc.streamlit.app/"
 st.write(f"OCR: [Enlace]({url})")

 st.subheader("Pagina WEB Clasica")
 image = Image.open('Pag_Class.jpg')
 st.image(image, width=190)
 st.write("Diseño de una Pagina WEB clasica .") 
 url = "https://introlpagelc.streamlit.app/"
 st.write(f"Pagina: [Enlace]({url})")
 
with col5: 
 st.subheader("Análisis de Datos")
 image = Image.open('Analisis_Datos.jpg')
 st.image(image, width=190)
 st.write("Permite hacer analisis de una Dataset.") 
 url = "ttps://dataagent-me6lrsfki8patgez9kpskj.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")
 
 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('REC_OCR.jpg')
 st.image(image, width=190)
 st.write("Identifica la información en una imagen o de Video, la selecciona y la almacena en Texto  .") 
 url = "https://ocr-audiolc.streamlit.app/"
 st.write(f"OCR: [Enlace]({url})")

 st.subheader("Pagina WEB Clasica")
 image = Image.open('Pag_Class.jpg')
 st.image(image, width=190)
 st.write("Diseño de una Pagina WEB clasica .") 
 url = "https://introlpagelc.streamlit.app/"
 st.write(f"Pagina: [Enlace]({url})")
