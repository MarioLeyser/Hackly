# components/story_introduction.py
import streamlit as st
from utils.state_manager import start_story_introduction

def display_story_introduction():
    """Muestra la introducción contextual a la historia seleccionada"""
    # Título de la historia
    if st.session_state.active_story == "amazon_voices":
        story_title = "Voces Silenciadas en la Amazonía"
    else:
        story_title = "Historia Interactiva"
    
    st.title(story_title)
    
    # Imagen destacada
    try:
        st.image(f"assets/story_covers/{st.session_state.active_story}.png", use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/800x400.png?text=Imagen+de+Historia", use_column_width=True)
    
    st.markdown("""
    ## Sobre esta experiencia
    
    InnoMentor te invita a vivir una historia interactiva donde tus decisiones 
    importan. No solo leerás sobre los desafíos que enfrentan las comunidades 
    indígenas en la Amazonía, sino que tendrás que tomar decisiones difíciles 
    que afectarán el desarrollo de la historia.
    
    Esta narrativa está inspirada en situaciones reales de comunidades que 
    enfrentan la tala ilegal y luchan por hacer oír su voz en un mundo 
    hiperconectado del que han sido excluidas.
    
    A medida que avances, descubrirás personajes complejos, situaciones 
    desafiantes y aprenderás sobre realidades que a menudo permanecen invisibles.
    
    **¿Estás listo para comenzar esta aventura?**
    """)
    
    if st.button("Comenzar Historia", key="start_story", use_container_width=True):
        start_story_introduction()