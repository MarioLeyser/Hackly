# components/introduction.py
import streamlit as st
from utils.state_manager import start_story

def display_introduction():
    """Muestra la introducción narrativa que establece el contexto de la historia"""
    st.title("🌿 Voces Silenciadas en la Amazonía")
    
    # Imagen de introducción
    try:
        st.image("assets/chapter_images/amazon_voices/chapter_0.png", use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/800x400.png?text=Viaje+por+el+río", use_column_width=True)
    
    st.markdown("""
    ## Introducción
    
    El bote se mece suavemente mientras avanzas por el río. Los árboles se alzan imponentes 
    a ambos lados, formando un túnel verde que parece no tener fin. Llevas tres días de viaje 
    desde la última ciudad con conexión a internet.
    
    Has venido a Saweto, una comunidad indígena en lo profundo de la Amazonía, después de 
    escuchar sobre sus problemas con la tala ilegal y cómo luchan por hacer oír su voz en un 
    mundo cada vez más conectado del que ellos están excluidos.
    
    No eres un experto, pero tienes genuino interés por entender y, si es posible, 
    colaborar en algo que marque una diferencia.
    
    Don Emilio, quien te guía río arriba, señala hacia delante.
    
    —Estamos llegando —dice con voz tranquila—. Ellos no reciben muchas visitas. 
    Algunos desconfían de extraños. Otros tienen esperanza en ellos. ¿Tú por qué has venido realmente?
    """)
    
    # Un simple campo de texto para que el usuario responda a la pregunta inicial
    user_response = st.text_area(
        "¿Qué le responderías a Don Emilio sobre tus motivos para venir a Saweto?",
        height=100
    )
    
    # Botón para continuar
    if st.button("Continuar"):
        if user_response:
            start_story(user_response)
        else:
            st.warning("Por favor, escribe tu respuesta antes de continuar.")