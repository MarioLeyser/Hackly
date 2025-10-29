import streamlit as st
import json
import boto3
import re
import time
from stories.amazon_voices.chapters import CHAPTERS

import streamlit as st
import json
import boto3
import re
import time
from stories.amazon_voices.chapters import CHAPTERS

def get_prerecorded_response(chapter_index):
    """
    Devuelve respuestas preescritas según el capítulo
    """
    prerecorded_responses = {
        0: {
            "narrative_response": "La comunidad escucha tu presentación con atención, formando un círculo alrededor del fuego central. Algunos asienten con interés, otros te miran con una mezcla de curiosidad y reserva, evaluándote en silencio. Los niños, inicialmente tímidos, comienzan a acercarse poco a poco, atraídos por la novedad de tu presencia. Rosa, una mujer de mediana edad con un porte que denota autoridad natural, se acerca a ti cuando terminas de hablar. Sus ojos reflejan décadas de experiencia y una cuidadosa evaluación de tus palabras. 'Gracias por compartir esto con nosotros,' te dice con una voz que el resto de la asamblea respeta. 'Mañana podremos hablar más. Por ahora, descansa y observa cómo vivimos aquí en Saweto.' Te indica dónde puedes descansar, mientras el resto de la comunidad continúa con sus conversaciones, ahora con un nuevo tema de discusión: tu llegada y lo que podría significar para ellos.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": ["Rosa - Líder local y organizadora de la comunidad"],
            "new_discoveries": ["La comunidad realiza asambleas nocturnas para discutir asuntos importantes"],
            "new_facts": ["La confianza debe ganarse gradualmente en esta comunidad"]
        },
        1: {
            "narrative_response": "Tu respuesta genera un vibrante debate entre los presentes. La luz del fuego baila en los rostros de la comunidad, revelando expresiones que van desde el entusiasmo hasta el escepticismo profundo. Un anciano levanta su mano arrugada y comparte una historia de cómo intentos anteriores de solucionar sus problemas habían fracasado, mientras algunos jóvenes argumentan con energía que esta vez podría ser diferente. Rosa, quien ha permanecido en silencio durante gran parte del intercambio, finalmente interviene con una voz que calma los ánimos encendidos. Sus ojos se encuentran con los tuyos con una mezcla de esperanza cautelosa y pragmatismo. 'Es interesante ver esto desde otra perspectiva,' dice, haciendo que todos guarden silencio para escucharla. 'Mañana Don Manuel quiere mostrarte algo en el bosque. Quizás entenderás mejor nuestros desafíos cuando veas con tus propios ojos lo que estamos perdiendo.' La asamblea se dispersa poco después, con pequeños grupos que continúan discutiendo tus palabras mientras regresan a sus hogares bajo el cielo estrellado.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": ["Don Manuel - Anciano respetado de la comunidad"],
            "new_discoveries": [],
            "new_facts": ["La comunidad enfrenta divisiones internas sobre cómo abordar sus problemas"]
        },
        2: {
            "narrative_response": "Don Manuel escucha tu respuesta con atención, su rostro surcado por arrugas permanece contemplativo mientras absorbe cada palabra. El viento susurra entre los árboles que aún quedan en pie, como si la naturaleza misma estuviera escuchando este intercambio. A lo lejos, un pájaro desconocido emite un canto melancólico que parece acompañar perfectamente el momento. Finalmente, el anciano asiente lentamente mientras su mirada permanece fija en el claro vacío donde antes se alzaba majestuoso el árbol. Sus manos callosas acarician la corteza de un tronco cercano, como quien consuela a un viejo amigo. 'Cada uno debe encontrar sus propias razones para seguir,' dice finalmente, con una voz que carga el peso de muchas pérdidas, pero también la sabiduría de quien ha sobrevivido a ellas. 'Gracias por compartir las tuyas.' Tras un momento de silencio compartido, continúan el recorrido por el bosque con paso lento pero decidido, atravesando senderos que Don Manuel conoce de memoria, con una mezcla de tristeza y determinación que parece unirlos a ambos en una comprensión más profunda de lo que está en juego.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["La relación espiritual entre la comunidad y árboles específicos del bosque"],
            "new_facts": ["La tala ha destruido lugares de importancia cultural y espiritual para la comunidad"]
        },
        3: {
            "narrative_response": "Elías escucha tus ideas con atención, sus ojos gradualmente iluminándose con un entusiasmo renovado que transforma su expresión previamente escéptica. El martilleo sobre el techo de la escuela se detiene momentáneamente mientras considera tus palabras, dejando que el sonido de la selva llene el silencio entre ustedes. Lejos del cliché del joven impaciente, muestra una reflexión madura que combina su frustración con una esperanza cautelosa. 'Nunca lo había pensado así,' dice mientras guarda su teléfono en el bolsillo, como si simbolizara un cambio de enfoque. 'Quizás no necesitamos esperar a que la tecnología llegue completamente para empezar a documentar lo que está pasando.' Sus manos, antes inquietas, ahora gesticulan con propósito mientras desarrolla la idea que has plantado. 'Conozco a chicos y chicas de otras comunidades, algunos han estudiado un poco más, otros tienen acceso ocasional a internet en el pueblo. Podríamos formar una red, combinar lo que cada uno puede hacer.' Se compromete a trabajar en tu propuesta con una energía contagiosa, mencionando nombres de jóvenes de comunidades vecinas que podrían estar interesados en colaborar. Por primera vez desde tu llegada, ves cómo una sugerencia comienza a transformarse en acción concreta, impulsada por quienes mejor conocen el terreno.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Métodos alternativos de comunicación que combinan lo analógico y digital"],
            "new_facts": ["Existe una red informal de jóvenes indígenas interesados en la tecnología"]
        },
        4: {
            "narrative_response": "Yuriko observa con fascinación mientras examinas la radio abandonada, sus ojos siguiendo atentamente cada movimiento de tus manos sobre el polvoriento equipo. La luz que filtra por la ventana forma patrones danzantes en el suelo de madera mientras trabajas, creando una atmósfera casi mágica en la pequeña habitación llena de tecnología olvidada. Tu respuesta hace que una sonrisa gradual ilumine su rostro juvenil, revelando un entusiasmo que contrasta con la melancolía del lugar. 'Mi abuelo dice que antes, todas las comunidades se conectaban así,' comenta ella con una mezcla de orgullo y nostalgia por algo que nunca experimentó personalmente. 'Compartían alertas cuando venían madereros ilegales, anunciaban nacimientos, organizaban encuentros.' Sus dedos trazan patrones en el polvo acumulado sobre una pila de cintas de casete, cada una etiquetada cuidadosamente con fechas y nombres de comunidades distantes. Entre los dos, identifican algunas partes que podrían repararse con materiales disponibles localmente, y Yuriko menciona a un tío que trabajó como técnico en la ciudad. Al final del día, aunque la radio sigue sin funcionar completamente, has plantado una semilla de posibilidad en la joven. Cuando te despides para ir a cenar, la encuentras organizando las cintas y limpiando cuidadosamente cada componente, como quien prepara un tesoro olvidado para su redescubrimiento.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Sistema de alertas comunitarias que existía anteriormente"],
            "new_facts": ["Las comunidades tenían redes de comunicación efectivas antes de la degradación de sus equipos"]
        },
        5: {
            "narrative_response": "Tu intervención en el acalorado debate genera un momento de pausa, como si el tiempo se detuviera brevemente para permitir que tus palabras penetren en la tensión del ambiente. Rostros que hace un momento estaban contraídos por la frustración o la indignación ahora muestran una expresividad más contemplativa. El fuego de la discusión no se extingue, pero sus llamas parecen menos destructivas y más iluminadoras. Rosa asiente lentamente, sus ojos evaluando las posibilidades que has presentado. 'Tiene sentido lo que dices,' admite con una voz que lleva el peso de alguien que ha visto demasiados conflictos sin resolver. Elías, aunque mantiene los brazos cruzados en una postura defensiva, muestra un cambio sutil en su mirada. 'Podríamos intentarlo,' concede con cautela, como quien prueba el primer escalón de un puente desconocido. La tensión en el ambiente disminuye poco a poco, y el espacio creado permite que voces que no habían participado comiencen a emerger. Sorprendentemente, algunos de los ancianos comienzan a compartir historias de cómo la comunidad ha navegado cambios significativos en el pasado, siempre buscando un balance entre preservación e innovación. Don Manuel, que hasta ahora había permanecido en silencio, cuenta cómo su propio abuelo resistió inicialmente la llegada de las primeras radios, solo para convertirse luego en el narrador de historias más popular en las transmisiones nocturnas.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Estrategias históricas de la comunidad para adaptarse al cambio"],
            "new_facts": ["El conflicto actual refleja tensiones similares que han surgido en otros momentos históricos"]
        },
        6: {
            "narrative_response": "La comunidad escucha tu propuesta con una atención que casi puedes palpar, como si cada palabra fuera una semilla que cae en tierra fértil pero cautelosa. El sol de la tarde proyecta largas sombras a través del espacio comunitario mientras hablas, creando un juego de luz y oscuridad que parece simbolizar la transformación que estás proponiendo. Un silencio reflexivo sigue a tus últimas palabras, ese tipo de silencio que no es vacío sino lleno de pensamientos en formación. Don Manuel es el primero en romperlo, su voz gastada pero clara atraviesa el espacio con una autoridad serena. 'Me gusta que has pensado en todos nosotros, en nuestros mayores y en nuestros niños,' dice, tocando el corazón de lo que hace que una propuesta sea verdaderamente comunitaria. Rosa, siempre práctica, añade: 'Es algo que podemos hacer con lo que tenemos, sin esperar ayuda que nunca llega.' Sus palabras resuenan con la experiencia de promesas externas incumplidas. Lo más sorprendente es la reacción de Elías, quien ha sido tu crítico más consistente. Se endereza y asiente con aprobación, sus ojos brillando con el reconocimiento de algo viable. 'Podría funcionar,' admite, rompiendo su habitual postura defensiva. Hay un murmullo creciente de acuerdo que recorre el círculo, y pronto varios miembros comienzan a ofrecer formas concretas en que podrían contribuir: una familia ofrece espacio para reuniones, otra menciona herramientas que tienen guardadas, alguien más conoce a una persona en la ciudad que podría ayudar. La semilla que has plantado parece estar echando raíces ante tus ojos, nutrida por la energía colectiva de una comunidad que comienza a ver posibilidades donde antes solo había obstáculos.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["El poder de las propuestas concretas para unificar visiones divergentes"],
            "new_facts": ["La comunidad valora las soluciones que reconocen tanto sus limitaciones como sus fortalezas"]
        },
        7: {
            "narrative_response": "Rosa sonríe ante tu respuesta, una sonrisa que transmite tanto alivio como reconocimiento. 'Así es como sabemos que alguien realmente entiende nuestro camino,' dice con una calidez que no había mostrado antes. 'El río nunca fluye en línea recta, siempre encuentra su camino alrededor de las piedras.' Su metáfora captura perfectamente la esencia de la adaptabilidad que has propuesto, resonando con la filosofía de vida de la comunidad que has llegado a apreciar durante tu estancia. En los días siguientes, implementas los cambios con un enfoque renovado, uno que abraza la incertidumbre como parte del proceso. Los obstáculos que antes parecían frustrantes ahora revelan nuevas oportunidades de colaboración. Los ancianos, inicialmente confundidos por el proyecto original, ahora aportan su sabiduría para resolver problemas prácticos, compartiendo técnicas tradicionales que resultan sorprendentemente efectivas. Los jóvenes, liderados por Elías, contribuyen con su energía y perspectivas frescas, encontrando soluciones creativas a limitaciones técnicas. Incluso los niños participan, convirtiéndose en mensajeros entusiastas entre diferentes grupos de trabajo. Lo que comenzó como una serie de contratiempos se transforma gradualmente en un proceso orgánico de aprendizaje colectivo. Una tarde, mientras observas a diferentes generaciones trabajando juntas para adaptar tu idea original en algo que verdaderamente les pertenece, comprendes que el éxito no se mide en la implementación perfecta de un plan, sino en la capacidad de una comunidad para apropiarse del proceso y transformarlo en algo auténticamente suyo.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["El valor de los fracasos visibles como oportunidades de aprendizaje colectivo"],
            "new_facts": ["La comunidad responde mejor a la honestidad sobre los errores que a promesas perfectas"]
        },
        8: {
            "narrative_response": "Tu propuesta de colaboración intergeneracional es recibida con un entusiasmo que transforma el ambiente de la reunión. Es como si hubieras puesto palabras a algo que la comunidad sentía pero no había articulado, una visión que honra tanto su pasado como su futuro. El espacio comunitario, normalmente ordenado en jerarquías implícitas, comienza a reorganizarse espontáneamente en grupos de trabajo que cruzan las fronteras habituales de edad y rol social. Don Manuel, cuya voz siempre ha llevado el peso de la tradición, ahora se sienta rodeado de jóvenes atentos mientras ofrece enseñar las historias tradicionales que solo él conoce en su totalidad. 'Estas historias son mapas,' explica, 'no solo del territorio, sino de quiénes somos.' Al mismo tiempo, Elías, quien antes veía a los ancianos como obstáculos para el progreso, ahora muestra con paciencia sorprendente cómo usar una cámara digital prestada para documentar lugares sagrados y prácticas culturales. Sus explicaciones están llenas de respeto, desprovistas de la condescendencia que a menudo caracteriza estos intercambios. En un rincón, Yuriko ha tomado la iniciativa de coordinar un grupo de adolescentes que sirven de puente entre ambos mundos, aprendiendo simultáneamente las narrativas tradicionales y las herramientas digitales. 'Esto es diferente,' observa Rosa, parada a tu lado mientras contempla la escena con una mezcla de asombro y esperanza. 'No es solo un proyecto, es una forma nueva de trabajar juntos, de ser comunidad.' Sus palabras capturan la esencia de lo que está ocurriendo: la comunidad comienza a moverse con un ritmo propio, redescubriendo su identidad colectiva a través de un proceso donde cada persona, desde la más anciana hasta la más joven, encuentra su lugar y su contribución única.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Metodologías de trabajo que honran conocimientos diversos entre generaciones"],
            "new_facts": ["Las soluciones más sostenibles surgen cuando cada grupo se siente valorado y necesario"]
        },
        9: {
            "narrative_response": "Tu respuesta sobre el control de la narrativa resuena profundamente con la comunidad, como si hubieras tocado una cuerda que vibra con décadas de historias mal contadas y voces silenciadas. El salón comunal, iluminado por la luz dorada del atardecer que se filtra entre las tablas de madera, se llena de una energía nueva, una determinación colectiva que es casi palpable. Rostros que antes mostraban preocupación ahora reflejan una resolución nacida del reconocimiento de un derecho fundamental: el derecho a contar su propia historia. Rosa, siempre la pragmática del grupo, no pierde tiempo y organiza de inmediato un consejo para establecer protocolos claros. 'Los periodistas y las ONGs tendrán que seguir nuestras reglas,' afirma con una firmeza que no admite discusión, mientras anota puntos clave en una libreta desgastada. 'No más fotografías sin permiso, no más citar fuera de contexto.' Don Manuel, cuya sabiduría ha sido frecuentemente malinterpretada por visitantes externos, sugiere un sistema donde los testimonios sean siempre revisados por quienes los compartieron antes de ser publicados. 'Las palabras son como semillas,' dice el anciano, 'debemos cuidar dónde y cómo se plantan.' Mientras tanto, Elías, quien ha experimentado la frustración de ver representaciones superficiales de su cultura en redes sociales, propone talleres para que los jóvenes aprendan a documentar sus propias historias, combinando técnicas tradicionales de narración con medios digitales. La reunión se extiende hasta entrada la noche, con ideas fluyendo libremente en un espacio donde todos se sienten autorizados a contribuir. Más tarde, mientras ayudas a Rosa a organizar las notas del encuentro, ella te confía con una mezcla de sorpresa y empoderamiento: 'Nunca habíamos pensado que teníamos derecho a controlar cómo se cuenta nuestra historia. Siempre sentimos que era un privilegio que otros nos escucharan, no un derecho exigir ser entendidos correctamente.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Protocolos de representación y control narrativo desarrollados por la comunidad"],
            "new_facts": ["El acto de definir cómo quieren ser representados es en sí mismo empoderador"]
        },
        10: {
            "narrative_response": "La comunidad escucha tu propuesta final con un silencio respetuoso que habla más que cualquier aplauso. El círculo formado por los habitantes de Saweto parece contener toda la historia de estos meses compartidos: las dudas iniciales, los momentos de tensión, los pequeños triunfos, las lecciones aprendidas. La luz del atardecer baña el espacio comunitario, proyectando sombras alargadas que parecen conectar a cada persona presente en una red invisible de experiencias compartidas. Tus palabras finales resuenan en este espacio sagrado, no como una conclusión, sino como el comienzo de algo que continuará mucho después de tu partida. Cuando terminas, el silencio se extiende por varios segundos, ese tipo de silencio que indica que tus palabras están siendo absorbidas, procesadas, integradas en el tejido colectivo. Don Manuel es el primero en hablar, su voz cargando el peso y la dignidad de muchas generaciones: 'Has aprendido nuestro camino,' dice simplemente, pero en su mirada hay un reconocimiento que va más allá de las palabras, una validación que sólo él, con su historia de escepticismo inicial, puede otorgar. Rosa, cuyo pragmatismo ha sido un ancla durante todo el proceso, añade con una sonrisa genuina: 'Lo que propones nos permitirá continuar cuando ya no estés aquí. No depende de ti, ni de tecnología que no podemos mantener, sino de lo que hemos construido juntos.' Quizás lo más significativo es la transformación en Elías, que al principio era tu crítico más vocal. Ahora está completamente comprometido, ya organizando en su mente los próximos pasos mientras asiente con entusiasmo. La tarde se transforma gradualmente en una celebración no planificada, donde se comparten historias que entrelazan el pasado con visiones del futuro. La comida aparece, la música surge espontáneamente, y percibes un sentido de comunidad renovada que es el verdadero logro de estos meses. Antes de que todos se retiren a descansar, Rosa se acerca a ti en un momento tranquilo y te confiesa con una mezcla de vulnerabilidad y gratitud: 'Cuando llegaste, pensé que serías como los otros visitantes, lleno de ideas que no entienden nuestra realidad. Me alegra haberme equivocado. Has aprendido a escuchar, y nosotros hemos aprendido a hacernos oír.'",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["El verdadero impacto se mide en la capacidad de la comunidad para continuar por sí misma"],
            "new_facts": ["Las mejores estrategias combinan tradición, innovación y autonomía local"]
        },
        "default": {
            "narrative_response": "Tu respuesta es recibida con interés por la comunidad, generando un murmullo de conversaciones que se entrelazan como las ramas de los árboles circundantes. Los rostros a tu alrededor reflejan una gama de reacciones: algunos muestran entusiasmo inmediato, otros una consideración cautelosa, pero todos están genuinamente comprometidos con la discusión que has iniciado. El espacio comunitario, normalmente ordenado en líneas invisibles de jerarquía y tradición, parece reorganizarse sutilmente mientras las ideas fluyen entre generaciones. Se inicia una conversación animada sobre los próximos pasos a seguir y cómo implementar estas ideas de manera práctica, adaptándolas a las realidades y recursos locales. Don Manuel, el anciano respetado cuya opinión suele marcar el tono de las decisiones colectivas, asiente pensativamente mientras acaricia su barbilla con dedos arrugados por décadas de trabajo en la selva. Rosa, siempre atenta a los detalles prácticos, toma notas en un cuaderno gastado, dibujando ocasionalmente diagramas que conectan personas y tareas. 'Tendremos que discutir esto más a fondo,' dice ella con una autoridad tranquila, 'pero hay elementos que podemos comenzar a trabajar de inmediato.' Sus palabras actúan como un puente entre la reflexión y la acción, característica de una comunidad que ha aprendido que las buenas ideas deben traducirse en pasos concretos para sobrevivir. Mientras observas el intercambio que has catalizado, percibes algo nuevo en el ambiente: una sensación de propósito compartido que trasciende las divisiones que habías notado anteriormente, como si tu propuesta hubiera iluminado un camino donde distintas visiones pueden converger sin perderse.",
            "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
            "new_characters": [],
            "new_discoveries": ["Nuevas formas de colaboración entre distintas generaciones"],
            "new_facts": ["La combinación de conocimiento tradicional y nuevas ideas puede crear soluciones innovadoras"]
        }
    }
    
    # Devolver la respuesta pregrabada para este capítulo o una genérica si no existe
    return prerecorded_responses.get(chapter_index, prerecorded_responses["default"])

def process_user_response(user_response, chapter_index):
    """
    Procesa la respuesta del usuario usando Claude y devuelve la respuesta narrativa
    y los cambios en recursos/descubrimientos
    """
    # Verificar si debemos usar respuestas pregrabadas
    if st.session_state.get("use_pregrabadas", False):
        return get_prerecorded_response(chapter_index)
    
    try:
        # Obtener el contexto del capítulo actual
        chapter = CHAPTERS[chapter_index]
        
        # Construir un prompt para Claude (resto del código igual)
        prompt = f"""
        Contexto: Estamos en el capítulo {chapter_index + 1} - {chapter['title']} de una novela ligera interactiva sobre comunidades indígenas en la Amazonía.
        
        Narrativa del capítulo: {chapter['narrative']}
        
        Pregunta al usuario: {chapter['prompt']}
        
        Respuesta del usuario: {user_response}
        
        Por favor, genera:
        1. Una respuesta narrativa que continúe la historia basándose en lo que ha dicho el usuario (aproximadamente 3-4 párrafos)
        2. Cambios en los recursos del usuario (confianza, knowledge, influence) en una escala de -1 a +1 para cada uno
        3. Nuevos personajes, descubrimientos o hechos importantes que deberían añadirse al cuaderno de campo
        
        Tu respuesta debe seguir estrictamente este formato JSON, sin incluir nada adicional:
        {{
          "narrative_response": "Texto narrativo que continúa la historia...",
          "resource_changes": {{
            "confidence": 1,
            "knowledge": 0,
            "influence": -1
          }},
          "new_characters": ["Nombre - Descripción breve"],
          "new_discoveries": ["Descubrimiento importante"],
          "new_facts": ["Hecho relevante"]
        }}
        
        Asegúrate de que el JSON sea válido: usa comillas dobles para las claves y strings, evita caracteres de control o especiales que podrían romper el JSON.
        """
        
        # Crear una sesión de boto3 con el perfil específico
        session = boto3.Session(profile_name='fiee')
        # Usar la sesión para crear el cliente de bedrock-runtime
        bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')
        
        # Añadir sistema de reintentos
        max_retries = 5
        retry_delay = 2 
        
        for attempt in range(max_retries):
            try:
                response = bedrock_runtime.invoke_model(
                    modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
                    body=json.dumps({
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 2000,
                        "temperature": 0.7,
                        "messages": [
                            {"role": "user", "content": prompt}
                        ]
                    })
                )
                
                break
                
            except bedrock_runtime.exceptions.ThrottlingException as e:
                if attempt < max_retries - 1: 
                    wait_time = retry_delay * (2 ** attempt) 
                    st.warning(f"Demasiadas solicitudes. Reintentando en {wait_time} segundos...")
                    time.sleep(wait_time)
                else:
                    raise
        
        # Procesar respuesta
        response_body = json.loads(response['body'].read().decode('utf-8'))
        ai_response = response_body["content"][0]["text"]
        
        # Depuración - Ver la respuesta cruda
        #st.write("Debug - Respuesta cruda:")
        #st.code(ai_response)
        
        # Extraer el JSON
        json_pattern = r'(\{[\s\S]*\})'
        json_match = re.search(json_pattern, ai_response)
        
        if json_match:
            json_str = json_match.group(1)
            # Limpiar caracteres de control
            json_str = re.sub(r'[\x00-\x1F\x7F]', '', json_str)
            ai_response_json = json.loads(json_str)
        else:
            # Si no podemos extraer JSON, creamos una respuesta estructurada manualmente
            ai_response_json = {
                "narrative_response": ai_response,
                "resource_changes": {"confidence": 0, "knowledge": 0, "influence": 0},
                "new_characters": [],
                "new_discoveries": [],
                "new_facts": []
            }
        
        return ai_response_json
        
    except Exception as e:
        st.error(f"Error al procesar la respuesta: {str(e)}")
        st.error(f"Tipo de error: {type(e)}")
        import traceback
        st.error(traceback.format_exc())
        
        # Si hay error, usar respuestas pregrabadas como fallback
        return get_prerecorded_response(chapter_index)