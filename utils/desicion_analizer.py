# utils/decision_analyzer.py

def analyze_initial_response(response):
    """
    Analiza la primera respuesta del usuario para detectar tendencias iniciales
    
    Args:
        response: Texto de respuesta del usuario
    
    Returns:
        dict: Diccionario con valores para cada patrón de decisión
    """
    patterns = {
        "empathetic": 0,
        "technological": 0,
        "community": 0,
        "individual": 0,
        "creative": 0
    }
    
    # Palabras clave para cada patrón
    empathetic_keywords = ["escuchar", "entender", "aprender", "conocer", "respeto", "cultura"]
    technological_keywords = ["tecnología", "comunicación", "internet", "redes", "digital", "solución"]
    community_keywords = ["comunidad", "juntos", "colectivo", "grupo", "todos", "participar"]
    individual_keywords = ["yo", "puedo", "traigo", "ofrezco", "mi experiencia", "tengo"]
    creative_keywords = ["crear", "imaginar", "diferente", "nuevo", "innovar", "alternativa"]
    
    # Convertir a minúsculas para análisis
    response_lower = response.lower()
    
    # Contar ocurrencias de palabras clave
    for keyword in empathetic_keywords:
        if keyword in response_lower:
            patterns["empathetic"] += 1
            
    for keyword in technological_keywords:
        if keyword in response_lower:
            patterns["technological"] += 1
            
    for keyword in community_keywords:
        if keyword in response_lower:
            patterns["community"] += 1
            
    for keyword in individual_keywords:
        if keyword in response_lower:
            patterns["individual"] += 1
            
    for keyword in creative_keywords:
        if keyword in response_lower:
            patterns["creative"] += 1
    
    return patterns