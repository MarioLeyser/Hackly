# utils/state_manager.py (versión optimizada)
import streamlit as st
    
def init_session_state():
    """Inicializa el estado de la sesión si no existe"""
    if "initialized" not in st.session_state:
        # Flags de navegación
        st.session_state.initialized = True
        st.session_state.show_welcome = True
        st.session_state.show_story_selector = False
        st.session_state.show_story_introduction = False
        st.session_state.show_introduction = False
        st.session_state.show_notebook = False
        st.session_state.show_feedback = False
        
        # Flag para respuestas pregrabadas
        st.session_state.use_pregrabadas = False
        
        # Estado de la historia
        st.session_state.active_story = None
        st.session_state.current_chapter = 0
        
        # Recursos del jugador
        st.session_state.resources = {
            "confidence": 2,  # Confianza inicial: 2/5
            "knowledge": 1,   # Conocimiento inicial: 1/5
            "influence": 3    # Influencia inicial: 3/5
        }
        
        # Información del personaje y decisiones
        st.session_state.character = {
            "decisions": []   # Historial de decisiones
        }
        
        # Contenido del cuaderno de campo
        st.session_state.notebook = {
            "characters": [],
            "discoveries": [],
            "facts": []
        }
        
        # Análisis de decisiones para retroalimentación
        st.session_state.decision_patterns = {
            "empathetic": 0,
            "technological": 0,
            "community": 0,
            "individual": 0,
            "creative": 0
        }

def go_to_story_selector():
    """Navega al selector de historias"""
    st.session_state.show_welcome = False
    st.session_state.show_story_selector = True
    st.rerun()  # Añadido para eliminar el doble clic

def load_story(story_id):
    """Carga una historia específica"""
    st.session_state.active_story = story_id
    st.session_state.show_story_selector = False
    st.session_state.show_story_introduction = True
    st.rerun()  # Añadido para eliminar el doble clic

def start_story_introduction():
    """Comienza la introducción de la historia"""
    st.session_state.show_story_introduction = False
    st.session_state.show_introduction = True
    st.rerun()  # Añadido para eliminar el doble clic

def start_story(initial_response):
    """Comienza la historia después de la introducción"""
    # Registrar la primera respuesta del usuario
    st.session_state.character["decisions"].append({
        "chapter": "intro",
        "decision": initial_response
    })
    
    # Desactivar la introducción y comenzar el primer capítulo
    st.session_state.show_introduction = False
    st.session_state.current_chapter = 0
    st.rerun()  # Añadido para eliminar el doble clic

def open_notebook():
    """Abre el cuaderno de campo"""
    st.session_state.show_notebook = True
    st.rerun()  # Añadido para eliminar el doble clic

def close_notebook():
    """Cierra el cuaderno de campo"""
    st.session_state.show_notebook = False
    st.rerun()  # Añadido para eliminar el doble clic

def next_chapter():
    """Avanza al siguiente capítulo"""
    st.session_state.current_chapter += 1
    # No añadimos st.rerun() aquí porque ya se llama en chapter_view.py

def show_feedback():
    """Muestra la pantalla de retroalimentación final"""
    st.session_state.show_feedback = True
    # No añadimos st.rerun() aquí porque ya se llama en chapter_view.py