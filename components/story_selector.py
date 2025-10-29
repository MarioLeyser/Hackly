# components/story_selector.py
import streamlit as st
from utils.state_manager import load_story

def display_story_selector():
    """Muestra el selector de historias disponibles y próximas"""
    st.title("Selecciona una Historia")
    st.markdown("---")
    
    # Crear 3 columnas para las tarjetas de historias
    col1, col2, col3 = st.columns(3)
    
    # Historia disponible
    with col1:
        try:
            st.image("assets/story_covers/amazon_voices.png", use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x225.png?text=Voces+Silenciadas", use_column_width=True)
            
        st.markdown("""
        ### Voces Silenciadas en la Amazonía
        
        Explora los desafíos de comunidades indígenas amazónicas enfrentando la tala ilegal y la desconexión.
        """)
        if st.button("Comenzar", key="start_amazon"):
            load_story("amazon_voices")
    
    # Próximamente 1
    with col2:
        try:
            st.image("assets/story_covers/upcoming_1.png", use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x225.png?text=Próximamente", use_column_width=True)
            
        st.markdown("""
        ### Aguas Contaminadas
        
        _Próximamente_
        
        Una comunidad lucha contra la contaminación minera de su principal fuente de agua.
        """)
        st.button("Próximamente", key="upcoming_1", disabled=True)
    
    # Próximamente 2
    with col3:
        try:
            st.image("assets/story_covers/upcoming_2.png", use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x225.png?text=Próximamente", use_column_width=True)
            
        st.markdown("""
        ### Saberes Ancestrales
        
        _Próximamente_
        
        Recupera conocimientos tradicionales antes de que desaparezcan con los últimos guardianes.
        """)
        st.button("Próximamente", key="upcoming_2", disabled=True)