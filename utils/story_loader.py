# utils/story_loader.py

def get_available_stories():
    """
    Devuelve una lista de historias disponibles
    
    Por ahora solo devuelve la historia de la Amazonía, pero está preparado
    para cuando se añadan más historias en el futuro.
    
    Returns:
        list: Lista de diccionarios con información de las historias
    """
    return [
        {
            "id": "amazon_voices",
            "title": "Voces Silenciadas en la Amazonía",
            "description": "Explora los desafíos de comunidades indígenas amazónicas afectadas por tala ilegal, falta de conectividad y ausencia estatal.",
            "status": "available",
            "image": "amazon_voices.jpg"
        },
        {
            "id": "contaminated_waters",
            "title": "Aguas Contaminadas",
            "description": "Una comunidad lucha contra la contaminación minera de su principal fuente de agua.",
            "status": "coming_soon",
            "image": "upcoming_1.jpg"
        },
        {
            "id": "ancestral_knowledge",
            "title": "Saberes Ancestrales",
            "description": "Recupera conocimientos tradicionales antes de que desaparezcan con los últimos guardianes.",
            "status": "coming_soon",
            "image": "upcoming_2.jpg"
        }
    ]

def load_story(story_id):
    """
    Carga la configuración de una historia específica
    
    Args:
        story_id: Identificador de la historia a cargar
        
    Returns:
        dict: Datos de configuración de la historia
    """
    if story_id == "amazon_voices":
        from stories.amazon_voices.story_config import STORY_CONFIG
        return STORY_CONFIG
    else:
        return None