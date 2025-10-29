# components/chapter_view.py
import streamlit as st
from stories.amazon_voices.chapters import CHAPTERS
from utils.ai_handler import process_user_response
from utils.state_manager import open_notebook, next_chapter, show_feedback

def display_chapter(chapter_index):
    """Muestra el capítulo actual y procesa la respuesta del usuario"""
    # Obtener datos del capítulo
    if chapter_index >= len(CHAPTERS):
        show_feedback()
        return
        
    chapter = CHAPTERS[chapter_index]
    
    # Verificar si estamos esperando la respuesta del usuario o mostrando la respuesta de la IA
    showing_response = "current_response" in st.session_state
    
    # Verificar si estamos procesando una respuesta
    processing_response = st.session_state.get("processing_response", False)
    
    # Mostrar título del capítulo
    st.title(f"Capítulo {chapter_index + 1}: {chapter['title']}")
    
    # Mostrar imagen del capítulo
    try:
        image_path = f"assets/chapter_images/amazon_voices/{chapter['image_path']}"
        st.image(image_path, use_container_width=True)
    except:
        st.image("https://via.placeholder.com/800x400.png?text=Imagen+del+Capítulo", use_column_width=True)
    
    # Mostrar narrativa
    st.markdown(chapter["narrative"])
    
    if showing_response:
        # ESTADO 2: Mostrar respuesta de la IA y botón para continuar al siguiente capítulo
        st.markdown("---")
    
        # Mostrar indicador si estamos usando respuestas pregrabadas
        if st.session_state.get("use_pregrabadas", False):
           st.info("📝 En este modo, los recursos no se actualizarán", icon="ℹ️")
    
        st.markdown("### Respuesta")
        st.markdown(st.session_state.current_response["narrative_response"])
        
        # Botón para avanzar al siguiente capítulo
        if st.button("Continuar al siguiente capítulo", key="next_chapter", use_container_width=True):
            # Limpiar la respuesta actual y el estado de procesamiento
            if "current_response" in st.session_state:
                del st.session_state.current_response
            
            if "processing_response" in st.session_state:
                del st.session_state.processing_response
                
            # Avanzar al siguiente capítulo
            if chapter_index >= len(CHAPTERS) - 1:
                show_feedback()
            else:
                next_chapter()
            
            # Recargar la página
            st.rerun()
        
    else:
        # ESTADO 1: Mostrar prompt y campo para respuesta del usuario
        st.markdown(f"### {chapter['prompt']}")
        
        # Campo para la respuesta del usuario
        user_response = st.text_area("Tu respuesta:", height=150)
        
        # Botones de acción
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Modificar el botón para que se deshabilite durante el procesamiento
            notebook_button = st.button(
                "📔 Abrir Cuaderno de Campo", 
                use_container_width=True,
                disabled=processing_response  # Deshabilitar durante el procesamiento
            )
            
            # Solo abrir el cuaderno si no estamos procesando
            if notebook_button and not processing_response:
                open_notebook()
        
        with col2:
            # Deshabilitar el botón si estamos procesando una respuesta
            send_button = st.button(
                "Enviar respuesta" if not processing_response else "Procesando...", 
                key="submit", 
                use_container_width=True,
                disabled=processing_response
            )
            
            if send_button and not processing_response:
                if user_response:
                    # Establecer el estado de procesamiento
                    st.session_state.processing_response = True
                    
                    # Forzar actualización para desactivar el botón
                    st.rerun()
                else:
                    st.warning("Por favor, escribe tu respuesta antes de continuar.")
        
        # Este bloque se ejecuta después del rerun si estamos procesando
        if processing_response:
            # Agregar un mensaje informativo visible
            st.info("Por favor espera mientras InnoMentorIA analiza tu respuesta...")
            
            # Mostrar indicador de carga
            with st.spinner("InnoMentorIA está generando la historia..."):
                # Procesar la respuesta con IA
                result = process_user_response(user_response, chapter_index)
            
            # Guardar la respuesta en el estado
            st.session_state.current_response = result
            
            # Guardar la decisión del usuario
            st.session_state.character["decisions"].append({
                "chapter": chapter_index,
                "decision": user_response
            })
            
            # Actualizar recursos
            st.session_state.recent_resource_changes = {}  # Inicializar cambios recientes
            for resource, change in result["resource_changes"].items():
                # Guardar el cambio reciente para mostrarlo
                st.session_state.recent_resource_changes[resource] = change
                
                # Actualizar el recurso
                st.session_state.resources[resource] += change
                # Asegurar que los recursos estén entre 0 y 5
                st.session_state.resources[resource] = max(0, min(5, st.session_state.resources[resource]))
            
            # Actualizar cuaderno
            if "new_characters" in result:
                for character in result["new_characters"]:
                    if character not in st.session_state.notebook["characters"]:
                        st.session_state.notebook["characters"].append(character)
            
            if "new_discoveries" in result:
                for discovery in result["new_discoveries"]:
                    if discovery not in st.session_state.notebook["discoveries"]:
                        st.session_state.notebook["discoveries"].append(discovery)
            
            if "new_facts" in result:
                for fact in result["new_facts"]:
                    if fact not in st.session_state.notebook["facts"]:
                        st.session_state.notebook["facts"].append(fact)
            
            # Quitar el estado de procesamiento ya que hemos terminado
            del st.session_state.processing_response
            
            # Recargar la página para mostrar la respuesta
            st.rerun()
        
        # En chapter_view.py
        if not showing_response and not processing_response:
            # Mostrar indicador de modo
            if st.session_state.get("use_pregrabadas", False):
                st.info("Modo offline (respuestas pregrabadas)", icon="ℹ️")
            else:
                st.success("Modo IA activo", icon="✅")