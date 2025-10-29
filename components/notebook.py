# components/notebook.py
import streamlit as st
from utils.state_manager import close_notebook

def display_notebook():
    """Muestra el cuaderno de campo con la información recopilada"""
    st.title("📔 Cuaderno de Campo")
    
    if st.button("← Volver a la historia", key="close_notebook"):
        close_notebook()
        st.rerun()
    
    # Crear tres pestañas para las diferentes secciones del cuaderno
    tab1, tab2, tab3 = st.tabs(["Personajes", "Descubrimientos", "Hechos Importantes"])
    
    # Pestaña de personajes
    with tab1:
        st.header("Personajes")
        if not st.session_state.notebook["characters"]:
            st.info("Aún no has conocido personajes destacables.")
        else:
            for character in st.session_state.notebook["characters"]:
                with st.expander(character.split(" - ")[0]):
                    st.write(character)
    
    # Pestaña de descubrimientos
    with tab2:
        st.header("Descubrimientos")
        if not st.session_state.notebook["discoveries"]:
            st.info("Aún no has realizado descubrimientos significativos.")
        else:
            for discovery in st.session_state.notebook["discoveries"]:
                st.markdown(f"• {discovery}")
    
    # Pestaña de hechos importantes
    with tab3:
        st.header("Hechos Importantes")
        if not st.session_state.notebook["facts"]:
            st.info("Aún no has registrado hechos importantes.")
        else:
            for fact in st.session_state.notebook["facts"]:
                st.markdown(f"• {fact}")
    
    # Sección para tomar notas personales
    st.markdown("---")
    st.header("Mis Notas")
    
    # Cargar notas existentes o crear nuevas
    if "personal_notes" not in st.session_state:
        st.session_state.personal_notes = ""
    
    # Campo para editar notas
    notes = st.text_area(
        "Escribe tus propias notas y observaciones:",
        value=st.session_state.personal_notes,
        height=200
    )
    
    # Guardar notas al cambiar
    if notes != st.session_state.personal_notes:
        st.session_state.personal_notes = notes
        st.success("Notas guardadas")