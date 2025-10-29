# components/feedback_display.py
import streamlit as st
from datetime import datetime

def display_feedback():
    """Muestra la retroalimentación personalizada al final de la historia"""
    st.title("🌿 Reflexión Final")
    
    # Verificar si estamos en modo offline
    use_pregrabadas = st.session_state.get("use_pregrabadas", False)
    
    # Imagen de cierre
    try:
        st.image("assets/ui/feedback_image.png", use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/800x400.png?text=Reflexión+Final", use_column_width=True)
    
    # Extraer patrones de decisión para personalizar el feedback
    patterns = st.session_state.decision_patterns
    dominant_pattern = max(patterns, key=patterns.get)
    
    # Mostrar la narrativa del impacto posterior
    st.markdown("## El legado en Saweto")
    
    if use_pregrabadas:
        # Versión offline - texto genérico
        st.markdown(generate_offline_epilogue())
    else:
        # Versión con IA - análisis personalizado
        epilogue = generate_personalized_epilogue(
            st.session_state.character["decisions"],
            st.session_state.resources,
            dominant_pattern
        )
        st.markdown(epilogue)
    
    # Mostrar la reflexión básica
    st.markdown("""
    ## Has completado tu viaje en Saweto
    
    Llegaste como extraño, y ahora te vas llevando historias, aprendizajes y quizás... 
    semillas de cambio.
    """)
    
    st.markdown("### 🧭 Tu camino")
    reflection_message = generate_reflection_message(dominant_pattern)
    st.markdown(reflection_message)
    
    # Mostrar estadísticas finales
    st.markdown("### 📊 Recursos finales")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Confianza", value=f"{st.session_state.resources['confidence']}/5")
    
    with col2:
        st.metric("Conocimiento", value=f"{st.session_state.resources['knowledge']}/5")
    
    with col3:
        st.metric("Influencia", value=f"{st.session_state.resources['influence']}/5")
    
    # Fecha de completado
    st.caption(f"Historia completada: {datetime.now().strftime('%d/%m/%Y')}")
    
    # Citas inspiradoras
    st.markdown("---")
    st.markdown("""
    > "Nosotros no estamos contra el desarrollo. Solo queremos que nos pregunten primero."
    > 
    > — Ruth Buendía, líder indígena ashaninka
    """)
    
    # Botón para reiniciar
    if st.button("Iniciar Nuevo Viaje", use_container_width=True):
        # Reiniciar el estado completamente
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def generate_offline_epilogue():
    """Genera un epílogo genérico para el modo offline"""
    return """
    Seis meses después de tu partida, la vida en Saweto ha experimentado cambios sutiles pero significativos. La radio comunitaria, reparada durante tu estancia, ahora funciona tres días a la semana, transmitiendo comunicados importantes y preservando historias ancestrales narradas por Don Manuel.

    Rosa ha establecido un comité de comunicación que coordina los esfuerzos para documentar las incursiones de taladores ilegales. Con ayuda de aliados en la ciudad, han logrado presentar evidencia ante autoridades regionales, consiguiendo mayor atención sobre el problema que llevaba años siendo ignorado.

    Elías, inspirado por las conversaciones contigo, ahora divide su tiempo entre la ciudad y Saweto. Ha capacitado a un pequeño grupo de jóvenes en el uso de teléfonos móviles para documentar tanto amenazas como conocimientos tradicionales. Una vez al mes, viaja al centro urbano más cercano para cargar y compartir esta información con organizaciones aliadas.

    Yuriko y otros adolescentes han formado un grupo cultural que combina tradiciones ancestrales con nuevas formas de expresión. Su primer proyecto fue crear un mapa de sitios sagrados y áreas amenazadas, utilizando símbolos tradicionales y fotografías modernas. Este mapa ahora cuelga con orgullo en el centro comunitario, recordando a todos la importancia de su territorio.

    Los desafíos continúan: la tala ilegal no ha cesado completamente y las divisiones internas a veces resurgen. Sin embargo, existe ahora un sentido de propósito compartido que antes faltaba. La comunidad ha descubierto formas de hacer oír su voz sin perder su identidad.

    Las voces de Saweto, anteriormente silenciadas, han comenzado a resonar más allá del bosque. Su historia continúa escribiéndose, no como víctimas pasivas, sino como protectores activos de su cultura y su tierra.
    """

def generate_personalized_epilogue(decisions, resources, dominant_pattern):
    """Genera un epílogo personalizado basado en las decisiones del usuario"""
    confidence = resources["confidence"]
    knowledge = resources["knowledge"]
    influence = resources["influence"]
    total_score = confidence + knowledge + influence
    
    # Analizar decisiones clave
    # Primera propuesta (capítulo 6)
    first_action_decision = next((d for d in decisions if d.get("chapter") == 6), None)
    tech_focused = first_action_decision and any(word in first_action_decision["decision"].lower() 
                                               for word in ["tecnología", "digital", "móvil", "internet", "computadora"])
    
    traditional_focused = first_action_decision and any(word in first_action_decision["decision"].lower() 
                                                      for word in ["tradición", "ancestral", "cultural", "oral", "ceremonia"])
    
    # Decisión sobre comunicación externa (capítulo 9)
    communication_decision = next((d for d in decisions if d.get("chapter") == 9), None)
    community_control = communication_decision and any(word in communication_decision["decision"].lower() 
                                                    for word in ["control", "propio", "autonomía", "decidir", "protocolo"])
    
    partnership_focused = communication_decision and any(word in communication_decision["decision"].lower() 
                                                      for word in ["alianza", "colaboración", "periodista", "organización", "cooperación"])
    
    # Construir el epílogo basado en análisis
    epilogue_parts = []
    
    # Introducción
    epilogue_parts.append("Seis meses después de tu partida de Saweto...")
    
    # Párrafo sobre el impacto general basado en la puntuación total
    if total_score >= 12:  # Impacto significativo
        epilogue_parts.append(f"""
        La comunidad ha experimentado una transformación notable. Los cambios que sembraste durante tu tiempo allí han echado raíces profundas y están dando frutos visibles. En la última asamblea general, Rosa comentó a los visitantes: "Aquí marcamos el tiempo como 'antes' y 'después' de este proyecto. Ha cambiado nuestra forma de vernos a nosotros mismos."
        """)
    elif total_score >= 8:  # Impacto moderado
        epilogue_parts.append(f"""
        Se perciben cambios importantes en la comunidad, aunque el camino de transformación apenas comienza. El proyecto que ayudaste a iniciar continúa avanzando con altibajos. "No ha sido fácil mantener el impulso," confesó Rosa en su última carta, "pero cada obstáculo superado nos fortalece como comunidad."
        """)
    else:  # Impacto limitado
        epilogue_parts.append(f"""
        Aunque los cambios visibles han sido modestos hasta ahora, las semillas que plantaste han comenzado a germinar. La comunidad enfrenta muchos de los mismos desafíos, pero con una perspectiva renovada. Como mencionó Don Manuel en un mensaje grabado: "Las transformaciones más profundas a veces son las que menos se ven al principio."
        """)
    
    # Párrafo sobre proyectos específicos basado en decisiones del capítulo 6
    if tech_focused:
        epilogue_parts.append(f"""
        El enfoque tecnológico que propusiste ha mostrado resultados sorprendentes. Elías ha conseguido tres teléfonos adicionales con cámaras resistentes y ha establecido un sistema para documentar tanto la tala ilegal como conocimientos tradicionales. Una pequeña estación solar, donada por una ONG que se interesó en el proyecto, permite cargar estos dispositivos. Cada dos semanas, alguien viaja al pueblo más cercano para subir los materiales recopilados a una plataforma digital que ha comenzado a atraer atención internacional.
        """)
    elif traditional_focused:
        epilogue_parts.append(f"""
        Tu énfasis en las metodologías tradicionales ha revitalizado prácticas culturales que estaban desvaneciéndose. El consejo de ancianos, liderado por Don Manuel, ha establecido sesiones regulares de narración oral donde se documentan historias, conocimientos sobre plantas medicinales y técnicas tradicionales. Estos encuentros, inicialmente pensados solo para preservación cultural, se han convertido en espacios de resolución de conflictos y toma de decisiones comunitarias, fortaleciendo la cohesión interna.
        """)
    else:
        epilogue_parts.append(f"""
        La iniciativa de comunicación que comenzaste ha evolucionado orgánicamente, combinando elementos tradicionales y modernos según las necesidades del momento. La radio comunitaria funciona dos veces por semana, alternando entre programas de historias ancestrales y actualizaciones sobre temas contemporáneos. Un pequeño grupo de jóvenes y ancianos colabora regularmente para asegurar que tanto la sabiduría tradicional como las nuevas ideas tengan espacio.
        """)
    # Párrafo sobre relaciones externas basado en decisiones del capítulo 9
    if community_control:
        epilogue_parts.append(f"""
        Los protocolos de comunicación que ayudaste a establecer han sido fundamentales. Cuando un equipo de documentalistas intentó filmar en Saweto sin seguir el proceso acordado, la comunidad unida les presentó sus términos claramente. Sorprendentemente, esto llevó a una colaboración mucho más respetuosa y fructífera. La comunidad ahora tiene voz en cómo se cuenta su historia, y varios medios han debido adaptar su enfoque para trabajar con Saweto, estableciendo un precedente importante para otras comunidades de la región.
        """)
    elif partnership_focused:
        epilogue_parts.append(f"""
        Las alianzas estratégicas que fomentaste han ampliado significativamente el alcance de las voces de Saweto. Un periodista que visitó durante tu estancia ha publicado una serie de artículos que generaron atención nacional. Una organización de derechos indígenas ahora incluye regularmente a representantes de Saweto en foros internacionales. Estas conexiones externas han proporcionado cierta protección contra los madereros ilegales, quienes ahora enfrentan mayor escrutinio público y legal.
        """)
    else:
        epilogue_parts.append(f"""
        La relación de la comunidad con el mundo exterior ha evolucionado gradualmente. Han aprendido a ser selectivos con quienes comparten su historia, evaluando cuidadosamente las intenciones de visitantes y organizaciones. Rosa ha emergido como una vocera efectiva en eventos regionales, mientras que algunos jóvenes como Elías manejan las comunicaciones digitales ocasionales. Mantienen un equilibrio cuidadoso entre visibilidad protectora y privacidad cultural.
        """)
    
    # Párrafo sobre impacto individual basado en los recursos principales
    if confidence >= 4:
        epilogue_parts.append(f"""
        El legado más visible de tu trabajo es la renovada confianza de la comunidad. Donde antes había resignación frente a las amenazas externas, ahora existe una determinación colectiva. En una reciente invasión de taladores, la respuesta fue inmediata y unificada. Don Manuel, quien solía ser reservado con extraños, ahora lidera delegaciones que se reúnen con autoridades. "Aprendimos que nuestra voz tiene poder cuando hablamos juntos," explicó en un mensaje que te enviaron.
        """)
    elif knowledge >= 4:
        epilogue_parts.append(f"""
        El sistema de documentación que ayudaste a crear se ha convertido en un recurso invaluable. La comunidad mantiene registros detallados de flora, fauna, incursiones ilegales y eventos culturales. Este archivo, que combina conocimientos tradicionales con observaciones contemporáneas, ha llamado la atención de investigadores y activistas ambientales. Un proyecto de conservación regional ahora busca replicar este modelo en otras comunidades, reconociendo el valor único de este enfoque.
        """)
    elif influence >= 4:
        epilogue_parts.append(f"""
        Tu enfoque en desarrollar liderazgos diversos ha transformado las dinámicas de poder en Saweto. Donde antes las decisiones recaían en unas pocas personas, ahora existe un consejo intergeneracional donde jóvenes como Yuriko comparten responsabilidades con ancianos como Don Manuel. Este nuevo equilibrio ha permitido respuestas más ágiles a desafíos y oportunidades. Comunidades vecinas han tomado nota, enviando representantes para aprender sobre este modelo de gobernanza.
        """)
    else:
        epilogue_parts.append(f"""
        Los efectos de tu trabajo se manifiestan de maneras sutiles pero importantes en la vida diaria de Saweto. Las conversaciones nocturnas ahora frecuentemente incluyen debates sobre el futuro de la comunidad, donde voces que antes permanecían calladas ahora participan activamente. Los niños y jóvenes muestran un renovado interés en aprender tanto habilidades tradicionales como modernas, comprendiendo que ambas son valiosas para su futuro.
        """)
    
    # Conclusión personalizada basada en el patrón dominante
    if dominant_pattern == "empathetic":
        epilogue_parts.append(f"""
        Las conexiones emocionales y la empatía que cultivaste siguen resonando. Rosa mencionó en su último mensaje: "Lo que más valoramos no fueron las soluciones específicas, sino cómo nos enseñaste a escucharnos mutuamente de nuevo. Esa lección permanece con nosotros cada día."
        """)
    elif dominant_pattern == "technological":
        epilogue_parts.append(f"""
        Las herramientas y sistemas que ayudaste a implementar continúan adaptándose y evolucionando según las necesidades locales. Como Elías comentó recientemente: "Ahora entendemos que la tecnología no es el objetivo, sino un medio para preservar nuestra cultura y defender nuestra tierra en el mundo contemporáneo."
        """)
    elif dominant_pattern == "community":
        epilogue_parts.append(f"""
        El sentido de propósito colectivo que fomentaste ha crecido más fuerte con el tiempo. Las asambleas comunitarias tienen mayor participación que nunca, y las decisiones reflejan un equilibrio entre diferentes necesidades e intereses. Como observó Don Manuel: "Hemos recordado que nuestra mayor fortaleza siempre ha sido nuestra unidad."
        """)
    elif dominant_pattern == "creative":
        epilogue_parts.append(f"""
        El espíritu de innovación y adaptación que inspiraste continúa floreciendo en formas inesperadas. La comunidad ha desarrollado soluciones creativas a nuevos desafíos, combinando conocimientos ancestrales con ideas contemporáneas. Como dijo Yuriko en un mensaje de voz: "Nos enseñaste que los límites solo existen en nuestra mente."
        """)
    elif dominant_pattern == "individual":
        epilogue_parts.append(f"""
        Los liderazgos que reconociste y nutriste ahora guían a la comunidad con confianza renovada. Personas que antes dudaban de sus capacidades han encontrado su voz y su lugar. "Tu confianza en nosotros nos ayudó a confiar en nosotros mismos," escribió Rosa en su última carta.
        """)
    else:
        epilogue_parts.append(f"""
        El legado de tu tiempo en Saweto continúa manifestándose de formas tanto esperadas como sorprendentes. La comunidad ha incorporado muchas de las lecciones compartidas, adaptándolas a su contexto único y cambiante.
        """)
    
    # Mensaje final esperanzador
    epilogue_parts.append(f"""
    Las voces de Saweto, que alguna vez fueron silenciadas, ahora resuenan cada vez más lejos. Su camino no está libre de obstáculos, pero avanzan con mayor confianza y claridad de propósito. Tu nombre se menciona frecuentemente en las reuniones comunitarias, un recordatorio de que incluso las conexiones breves pueden tener impactos duraderos cuando se basan en el respeto mutuo y la colaboración genuina.
    """)
    
    # Unir todas las partes del epílogo
    return "\n".join(epilogue_parts)

def generate_reflection_message(dominant_pattern):
    """Genera un mensaje de reflexión personalizado basado en el patrón dominante de decisiones"""
    if dominant_pattern == "empathetic":
        return """
        Tu camino se caracterizó por la **escucha atenta** y la **empatía**. Priorizaste entender antes de actuar.
        
        Al principio, tu enfoque fue cauteloso, pero con cada interacción fuiste construyendo puentes de confianza. Los ancianos de la comunidad apreciaron especialmente tu respeto por sus tradiciones y conocimientos.
        
        Esta sensibilidad te permitió descubrir capas de complejidad que permanecían ocultas para otros visitantes. Recuerda siempre que la empatía no es solo un valor, sino una poderosa herramienta de transformación.
        """
    elif dominant_pattern == "technological":
        return """
        Tu enfoque se inclinó hacia soluciones **tecnológicas e innovadoras**. Buscaste maneras de usar herramientas modernas para abordar problemas ancestrales.
        
        Tu visión pragmática abrió posibilidades que la comunidad no había considerado antes. Sin embargo, también descubriste que la tecnología sin contextualización cultural tiene limitaciones importantes.
        
        El puente que intentaste construir entre tradición y modernidad es complejo pero necesario. El verdadero desafío sigue siendo cómo integrar lo nuevo sin perder la esencia de lo ancestral.
        """
    elif dominant_pattern == "community":
        return """
        Tu enfoque se centró en el **poder colectivo** y las **soluciones comunitarias**. Entendiste que las respuestas más sostenibles nacen desde dentro.
        
        A lo largo de tu aventura, priorizaste decisiones que fortalecían los lazos internos y el liderazgo local. Tu habilidad para mediar entre diferentes visiones dentro de la comunidad fue particularmente valiosa.
        
        Has aprendido que el verdadero cambio no viene de soluciones impuestas, sino de procesos participativos donde cada voz cuenta, especialmente aquellas que han sido históricamente silenciadas.
        """
    elif dominant_pattern == "individual":
        return """
        Tu camino se destacó por tu **iniciativa individual** y **liderazgo directo**. No temiste tomar las riendas cuando fue necesario.
        
        Tu disposición para actuar y proponer soluciones concretas inspiró a otros. Sin embargo, también enfrentaste resistencias cuando tus ideas no resonaban con las necesidades locales.
        
        Has descubierto el delicado equilibrio entre liderar con determinación y crear espacios para que otros también lideren.
        """
    elif dominant_pattern == "creative":
        return """
        Tu enfoque se distinguió por soluciones **creativas e inesperadas**. Donde otros veían obstáculos, tú encontraste oportunidades para innovar.
        
        Tu capacidad para pensar lateralmente y conectar ideas aparentemente distantes abrió nuevos caminos para la comunidad. Tus propuestas poco convencionales, aunque inicialmente recibidas con escepticismo, demostraron ser valiosas.
        
        Has aprendido que la creatividad, cuando se nutre con respeto y conocimiento del contexto local, puede ser una poderosa herramienta para desafiar el statu quo y encontrar soluciones donde parecía no haberlas.
        """
    else:
        return """
        Tu camino fue **diverso y adaptativo**. En lugar de seguir un enfoque único, respondiste a cada situación de manera flexible.
        
        A veces escuchabas, otras proponías, en ocasiones mediabas. Esta versatilidad te permitió navegar la complejidad de Saweto con mayor facilidad, aunque quizás sin una dirección consistente.
        
        Has aprendido que las soluciones a problemas complejos raramente siguen un único enfoque, y que la adaptabilidad es tan importante como la consistencia.
        """