import streamlit as st
from PIL import Image

# Configuración de la página para que use todo el ancho
st.set_page_config(layout="wide")

# Estilos CSS mejorados
st.markdown(
    """
    <style>
    /* Fondo azul para la barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #0000FF !important;
    }

    /* Texto blanco en sidebar */
    section[data-testid="stSidebar"] .stText, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: white !important;
    }

    /* Estilo para alinear contenedores de aplicaciones */
    .app-container {
        height: 450px; /* Altura fija para que todo esté alineado */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    /* Forzar que las imágenes tengan el mismo tamaño */
    img {
        object-fit: cover;
        border-radius: 10px;
        height: 150px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.subheader("Luis Castañeda")    
    st.subheader("Como aplicar la IA")
    st.write("Herramientas desarrolladas para identificar la funcionalidad de la Inteligencia Artificial...")

st.title("Aplicabilidad de la IA")
st.subheader("Pruebas de Concepto aplicadas a IA")

# --- FUNCIÓN PARA RENDERIZAR CADA APP ---
def render_app(title, img_path, description, url, link_label):
    # Usamos subheader y limitamos el tamaño de la imagen para consistencia
    st.markdown(f"### {title}")
    try:
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    except:
        st.warning(f"No se encontró: {img_path}")
    
    # Altura mínima para el texto para evitar desalineación
    st.write(description)
    st.markdown(f"[{link_label}]({url})")

# --- ORGANIZACIÓN POR FILAS (Grid) ---

# Fila 1
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    render_app("Detección de Objetos", "Analisis_Imagenes.jpg", "Sistema que permite identificar con Video Objetos.", "https://yolov5-hpaetkatdrdpj4jkhy8qex.streamlit.app/", "Objetos")
with col2:
    render_app("Análisis de Imágenes", "Clasificar.jpg", "Aplicación que permite clasificar imágenes.", "https://multimodalgptlc.streamlit.app/", "Imágenes")
with col3:
    render_app("Clasificar Vehículos", "Clasificar_Motos.jpg", "Clasifica imágenes de Vehículos, Motos y Bicicletas.", "https://tmimglc.streamlit.app/", "Movimiento")
with col4:
    render_app("Clasificador de Flores", "Clasificar_Flores.jpg", "Identifica fotos de flores y las clasifica.", "https://tlflores-lc.streamlit.app/", "Flores")
with col5:
    render_app("Análisis de Datos", "Analisis_Datos.jpg", "Permite hacer análisis de un Dataset.", "https://dataagent-me6lrsfki8patgez9kpskj.streamlit.app/", "Datos")

st.divider() # Separador visual

# Fila 2
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    render_app("Sentimientos", "Sentimientos.jpg", "Identifica el contexto y valida el sentimiento.", "https://sentimientoslc.streamlit.app", "Sentimiento")
with col2:
    render_app("Traductor Voz", "Traductor.jpg", "Traduce mensajes de voz a otro idioma.", "https://traductor--textlc.streamlit.app/", "Traductor")
with col3:
    render_app("Texto a Audio", "Texto_Audio.jpg", "Conversión de un Texto a audio.", "https://speedtexttlc.streamlit.app/", "Audio")
with col4:
    render_app("OCR", "REC_OCR.jpg", "Identifica información en imagen o video.", "https://ocr-audiolc.streamlit.app/", "OCR")
with col5:
    render_app("Convoluciones", "Convulsiones.jpg", "Operación matemática para señales.", "https://convoluciones-lc.streamlit.app/", "Convoluciones")

st.divider()

# Fila 3
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    render_app("Nubes de Palabras", "Nube.jpg", "Analiza texto y crea nubes de palabras.", "https://wordcloud-nubelc.streamlit.app/", "Nube")
with col2:
    render_app("Chat GPT", "Chat.jpg", "Conversación con chatbot específico.", "https://chatbotopenailc.streamlit.app/", "Chat")
with col3:
    render_app("Chat Anthropic", "Chat_Ant.jpg", "Chat directamente con ML Anthropic.", "https://antchgptlc.streamlit.app", "Anthropic")
with col4:
    render_app("Web Clásica", "Pag_Class.jpg", "Diseño de una Página WEB clásica.", "https://introlpagelc.streamlit.app/", "Página")
with col5:
    render_app("Autoencoder", "Autoencoder.jpg", "Red neuronal para copiar entrada a salida.", "https://appaev.streamlit.app/", "Autoencoder")


# Fila 4
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    render_app("Detector de Numereos Escritos", "Detector_Numeros.jpg", "Analiza el número que se escribe en pizarra y pronostica .", "https://mnistpred-deteccionumeros.streamlit.app/", "Numeros")
with col2:
    render_app("Redes Neuronales Recurrentes", "Redes_Neuronales.jpg", "Agentes de IA e Interfaces Multimodales Generador de Texto LSTM.", "https://lstmnlp-oragfnp8t765eu2bgchvgs.streamlit.app/", "Red_Neuro")
with col3:
    render_app("Chat Anthropic", "Chat_Ant.jpg", "Chat directamente con ML Anthropic.", "https://antchgptlc.streamlit.app", "Anthropic")
with col4:
    render_app("Web Clásica", "Pag_Class.jpg", "Diseño de una Página WEB clásica.", "https://introlpagelc.streamlit.app/", "Página")
with col5:
    render_app("Autoencoder", "Autoencoder.jpg", "Red neuronal para copiar entrada a salida.", "https://appaev.streamlit.app/", "Autoencoder")
