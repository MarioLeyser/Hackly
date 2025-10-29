# app.py
import streamlit as st
from utils.state_manager import init_session_state
from components.welcome_screen import display_welcome_screen
from components.story_selector import display_story_selector
from components.story_introduction import display_story_introduction
from components.introduction import display_introduction
from components.chapter_view import display_chapter
from components.notebook import display_notebook
from components.feedback_display import display_feedback
from components.resource_tracker import display_resources

# Configuración inicial de la página
st.set_page_config(
    page_title="InnoMentor - Aventuras Interactivas",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Añadir CSS para mejorar la legibilidad del texto
st.markdown("""
<style>
    /* Limitar el ancho máximo del contenido para mejor legibilidad */
    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
    }
    
    /* Mejorar la legibilidad del texto narrativo */
    p {
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 1.2rem;
        max-width: 800px;
    }
    
    /* Añadir un poco de espacio después de los títulos */
    h1, h2, h3 {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar el estado de la sesión
init_session_state()

# Flujo principal de la aplicación
if st.session_state.show_welcome:
    display_welcome_screen()
elif st.session_state.show_story_selector:
    display_story_selector()
elif st.session_state.show_story_introduction:
    display_story_introduction()
elif st.session_state.show_introduction:
    display_introduction()
elif st.session_state.show_notebook:
    display_notebook()
elif st.session_state.show_feedback:
    display_feedback()
else:
    # Mostrar el capítulo actual
    display_chapter(st.session_state.current_chapter)
    
with st.sidebar:
    st.title("🌿 Recursos")
    display_resources()