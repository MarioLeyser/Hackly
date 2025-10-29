# components/resource_tracker.py (con líneas divisorias reorganizadas)
import streamlit as st
import random

def display_resources():
    """Muestra los recursos del jugador de forma visual con indicadores de cambio mejorados"""
    resources = st.session_state.resources
    
    # Obtener cambios recientes (si existen)
    recent_changes = st.session_state.get("recent_resource_changes", {})
    
    # Mostrar progreso en la historia
    from stories.amazon_voices.chapters import CHAPTERS
    current = st.session_state.current_chapter + 1
    total = len(CHAPTERS)
    st.markdown("### Progreso")
    st.progress(current/total)
    st.write(f"Capítulo {current} de {total}")
    
    # Función para mostrar cada recurso
    def display_resource(name, emoji, level, change=0):
        st.markdown(f"### {emoji} {name}", help=f"Nivel actual de {name.lower()}: {level}/5")
        
        # Mostrar puntos
        dots_html = ""
        for i in range(5):
            if i < level:
                dots_html += "● "
            else:
                dots_html += "○ "
        
        # Preparar indicador de cambio
        change_html = ""
        if change > 0:
            change_html = f"<span class='resource-change resource-increase'>+{change} ↑</span>"
        elif change < 0:
            change_html = f"<span class='resource-change resource-decrease'>{change} ↓</span>"
        
        # Mostrar puntos y cambio en la misma línea
        st.markdown(f"""
        <div style='display: flex; align-items: center;'>
            <div class='resource-dots'>{dots_html}</div>
            {change_html}
        </div>
        """, unsafe_allow_html=True)
    
    # Mostrar cada recurso
    display_resource("Confianza", "🤝", resources["confidence"], 
                    recent_changes.get("confidence", 0))
    
    display_resource("Conocimiento", "📚", resources["knowledge"], 
                    recent_changes.get("knowledge", 0))
    
    display_resource("Influencia", "✨", resources["influence"], 
                    recent_changes.get("influence", 0))
    
    # Añadir línea separadora entre recursos y consejos del mentor
    st.markdown("---")
    
    # Función para obtener consejos contextuales específicos para cada capítulo
    def get_chapter_advice(chapter_index):
        # Consejos detallados y específicos para cada capítulo
        chapter_advice = {
            0: [
                "Las primeras impresiones son cruciales. Muestra respeto por las costumbres locales y pregunta antes de actuar.",
                "Observa las dinámicas de poder: quién habla, quién escucha y quién toma las decisiones finales.",
                "La forma en que te presentas establecerá expectativas y posibilidades futuras. Sé honesto sobre tus objetivos.",
                "En comunidades con experiencias previas negativas, la transparencia es fundamental para construir confianza."
            ],
            1: [
                "Cuando te pregunten tu opinión tan directamente, reconoce primero lo que no sabes antes de ofrecer ideas.",
                "Las soluciones externas rara vez funcionan sin adaptación local. Enfatiza la colaboración, no la imposición.",
                "Pregúntate cómo tu presencia influye en la dinámica de la reunión. ¿Están todos expresando libremente sus ideas?",
                "A veces, lo más valioso que puedes aportar no es una respuesta, sino un marco para pensar diferentes posibilidades."
            ],
            2: [
                "Don Manuel está compartiendo no solo pérdida ambiental, sino la erosión de la memoria cultural asociada al paisaje.",
                "Este recorrido es una invitación a entender cómo el territorio es también un archivo de historias y relaciones.",
                "Cuando un anciano comparte un lugar así, está evaluando si puedes ver más allá de los árboles, hacia las conexiones invisibles.",
                "Considera la importancia del tiempo: lo que tomó décadas crecer se destruyó en horas. ¿Qué significa esto para las soluciones propuestas?"
            ],
            3: [
                "El dilema de Elías es común: las habilidades adquiridas fuera parecen inútiles si no pueden aplicarse en casa.",
                "La brecha digital va más allá del acceso a la tecnología; implica quién puede contar su historia al mundo.",
                "Considera soluciones híbridas que combinen métodos tradicionales con nuevas tecnologías accesibles localmente.",
                "Las herramientas digitales pueden ser poderosas, pero solo si son apropiadas y sostenibles en el contexto local."
            ],
            4: [
                "La radio representa más que un medio de comunicación; es un símbolo de la voz colectiva de la comunidad.",
                "A veces, recuperar herramientas del pasado puede ser más efectivo que introducir nuevas tecnologías.",
                "Busca entender por qué la radio dejó de funcionar - podría revelar obstáculos sociales además de técnicos.",
                "Considera cómo empoderar a jóvenes como Yuriko para que se apropien de los medios de comunicación comunitarios."
            ],
            5: [
                "Este conflicto refleja tensiones generacionales presentes en muchas comunidades que enfrentan cambios rápidos.",
                "Evita tomar partido inmediatamente. Busca los valores compartidos detrás de posiciones aparentemente opuestas.",
                "La clave no es elegir entre tradición y modernidad, sino crear puentes que permitan a la comunidad evolucionar sin perder su esencia.",
                "Observa quién no está hablando en este debate. A veces, las perspectivas más valiosas son las menos ruidosas."
            ],
            6: [
                "Una propuesta concreta demuestra que has estado escuchando. Intégra las preocupaciones de diferentes grupos.",
                "Las mejores soluciones son aquellas que la comunidad puede implementar y mantener después de tu partida.",
                "Considera cómo tu propuesta distribuye roles y responsabilidades. ¿Refuerza o desafía las estructuras de poder existentes?",
                "El momento de proponer acción es delicado - debe ser lo suficientemente ambicioso para inspirar y realista para implementar."
            ],
            7: [
                "Los obstáculos inesperados revelan suposiciones que no habías cuestionado. Usa esto como oportunidad de aprendizaje.",
                "La adaptación es una forma de respeto: muestra que valoras más el proceso y las personas que tu plan original.",
                "Involucra a la comunidad en la resolución de problemas. Las soluciones colectivas tienen mayor legitimidad.",
                "Recuerda que los fracasos visibles y honestos construyen más confianza que éxitos superficiales."
            ],
            8: [
                "El verdadero éxito ocurre cuando tu papel pasa de líder a facilitador. Celebra este cambio.",
                "Aprecia cómo cada generación aporta conocimientos distintos pero igual de valiosos al proceso.",
                "Documenta este momento de co-creación. Es un modelo que la comunidad puede replicar en futuros desafíos.",
                "La transferencia de habilidades es tan importante como la solución misma. ¿Quién puede enseñar a otros lo aprendido?"
            ],
            9: [
                "El control de la narrativa es un tema de poder. Considera quién decide qué historias se cuentan y cómo.",
                "Ayuda a establecer protocolos claros sobre cómo la comunidad quiere ser representada ante el mundo exterior.",
                "Las buenas intenciones externas pueden causar daño sin la guía adecuada. La comunidad debe liderar este proceso.",
                "Piensa en sistemas de retroalimentación para que la comunidad pueda evaluar cómo se cuenta su historia."
            ],
            10: [
                "Tu propuesta final debe enfocarse en fortalecer la autonomía y capacidades locales, no en mantener dependencias.",
                "Reflexiona sobre tu propio aprendizaje y cómo ha cambiado tu perspectiva desde tu llegada.",
                "Una estrategia sostenible considera amenazas externas pero se construye sobre fortalezas internas de la comunidad.",
                "El mayor regalo que puedes dejar no es tu solución, sino la confianza renovada de la comunidad en sus propias capacidades."
            ]
        }
        
        # Proporcionar consejos genéricos si el capítulo no está en la lista
        default_advice = [
            "Escucha atentamente las necesidades expresadas e implícitas de la comunidad.",
            "Considera cómo tus acciones afectarán las dinámicas locales a largo plazo.",
            "Busca soluciones que respeten tanto la tradición como la necesidad de adaptación."
        ]
        
        # Seleccionar aleatoriamente uno de los consejos para el capítulo actual
        selected_advice = random.choice(chapter_advice.get(chapter_index, default_advice))
        return selected_advice
    
    # Definir estilos CSS para animaciones y apariencia del mentor
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.3); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }
    .resource-change {
        display: inline-block;
        animation: pulse 1.5s infinite;
        font-weight: bold;
        margin-left: 10px;
        padding: 2px 8px;
        border-radius: 12px;
    }
    .resource-increase {
        background-color: rgba(76, 175, 80, 0.2);
        color: #4CAF50;
    }
    .resource-decrease {
        background-color: rgba(244, 67, 54, 0.2);
        color: #F44336;
    }
    .resource-dots {
        font-size: 24px;
        letter-spacing: 4px;
        margin-top: 0;
    }
    .mentor-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #4F8BF9;
        color: white;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        float: left;
    }
    .mentor-message {
        background-color: rgba(38, 39, 48, 0.8); /* Oscuro para combinar con tema Streamlit */
        border-left: 3px solid #4F8BF9;
        padding: 10px;
        margin: 10px 0;
        border-radius: 0 5px 5px 0;
        color: #fafafa;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sección de consejos del mentor (visible directamente después de recursos)
    st.markdown("### 💡 Consejos del Mentor")
    
    # Obtener consejo específico para el capítulo actual
    mentor_advice = get_chapter_advice(st.session_state.current_chapter)
    
    # Mostrar consejo del mentor con estilo
    st.markdown(f"""
    <div class="mentor-message">
        <div class="mentor-avatar">M</div>
        <p>{mentor_advice}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Añadir resumen del cuaderno
    with st.expander("📔 Resumen del Cuaderno"):
        st.write(f"**Personajes**: {len(st.session_state.notebook['characters'])}")
        st.write(f"**Descubrimientos**: {len(st.session_state.notebook['discoveries'])}")
        st.write(f"**Hechos importantes**: {len(st.session_state.notebook['facts'])}")
    
    # Limpiar los cambios recientes después de mostrarlos
    if hasattr(st.session_state, "recent_resource_changes"):
        st.session_state.recent_resource_changes = {}
    
    # Añadir línea separadora antes de opciones de desarrollo
    st.markdown("---")
    
    # Sección de opciones de desarrollo (expandible)
    with st.expander("⚙️ Opciones de desarrollo"):
        # Checkbox para alternar entre IA y respuestas pregrabadas
        current_value = st.session_state.get("use_pregrabadas", False)
        use_pregrabadas = st.checkbox(
            "Activar modo offline", 
            value=current_value,
            help="Activa esta opción para evitar llamados a la API y continuar la historia sin internet"
        )
        
        # Actualizar estado si cambia
        if use_pregrabadas != current_value:
            st.session_state["use_pregrabadas"] = use_pregrabadas
            st.toast("✅ Modo de respuestas cambiado" + 
                   (" a historia lineal" if use_pregrabadas else " a IA"))