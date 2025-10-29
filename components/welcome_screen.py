# components/welcome_screen.py
import streamlit as st
from utils.state_manager import go_to_story_selector

def display_welcome_screen():
    """Muestra la pantalla de bienvenida con logo del proyecto"""
    # Crear columnas para centrar el contenido
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Logo
        try:
            st.image("assets/ui/logo.png", use_container_width=True)
        except FileNotFoundError:
            st.title("🌿 Hackly")
            st.markdown("*Logo no encontrado. Añade el archivo en assets/ui/logo.png*")
        
        st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h1 style='margin-bottom: 20px;'>HACKLY ✨</h1>
            <p style='font-size: 1.2em; margin-bottom: 40px;'>Aventuras interactivas para inspirar cambio</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botón grande centrado
        if st.button("INICIAR AVENTURA", key="start_button", use_container_width=True):
            go_to_story_selector()