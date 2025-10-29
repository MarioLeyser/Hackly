# test_bedrock_sso.py
import boto3
import json
import streamlit as st

def test_bedrock_connection():
    """
    Prueba la conexión con AWS Bedrock utilizando SSO.
    """
    st.title("🧪 Prueba de conexión con AWS Bedrock (SSO)")
    
    with st.form("sso_test"):
        sso_profile = st.text_input("Perfil SSO (por defecto, usa el perfil activo)", value="fiee")
        region = st.text_input("Región de AWS", value="us-east-1")
        model_id = st.text_input("ID del modelo", value="anthropic.claude-3-5-sonnet-20240620-v1:0")
        test_prompt = st.text_area("Prompt de prueba", value="Por favor responde con una frase corta: ¿Cómo estás hoy?")
        
        submitted = st.form_submit_button("Probar conexión")
    
    if submitted:
        with st.spinner("Conectando con AWS Bedrock..."):
            try:
                # Crear sesión con el perfil especificado
                st.info(f"Intentando crear sesión con perfil: {sso_profile}")
                if sso_profile:
                    session = boto3.Session(profile_name=sso_profile)
                else:
                    session = boto3.Session()
                
                # Crear cliente para Bedrock
                st.info(f"Creando cliente bedrock-runtime en región: {region}")
                bedrock_runtime = session.client('bedrock-runtime', region_name=region)
                
                # Preparar payload para el modelo
                payload = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 100,
                    "temperature": 0.7,
                    "messages": [
                        {"role": "user", "content": test_prompt}
                    ]
                }
                
                # Invocar el modelo
                st.info(f"Invocando modelo: {model_id}")
                response = bedrock_runtime.invoke_model(
                    modelId=model_id,
                    body=json.dumps(payload)
                )
                
                # Procesar respuesta
                response_body = json.loads(response['body'].read().decode('utf-8'))
                ai_response = response_body["content"][0]["text"]
                
                # Mostrar resultados
                st.success("¡Conexión exitosa!")
                st.subheader("Respuesta del modelo:")
                st.write(ai_response)
                
                # Mostrar detalles técnicos
                with st.expander("Detalles técnicos"):
                    st.json({"model_id": model_id, 
                            "profile": sso_profile, 
                            "region": region, 
                            "response_type": type(response).__name__,
                            "content_type": response.get('contentType', 'N/A')})
                
            except Exception as e:
                st.error(f"Error al conectar con AWS Bedrock: {str(e)}")
                st.error(f"Tipo de error: {type(e).__name__}")
                
                import traceback
                with st.expander("Detalles del error"):
                    st.code(traceback.format_exc())
                
                # Sugerencias basadas en tipos de error comunes
                if "ResourceNotFoundException" in str(e):
                    st.warning("El modelo especificado podría no existir o no estar disponible en esta región.")
                elif "AccessDeniedException" in str(e):
                    st.warning("Problema de permisos. Verifica que tu perfil SSO tenga acceso a Bedrock.")
                elif "ExpiredTokenException" in str(e):
                    st.warning("Tu sesión de SSO ha expirado. Inicia sesión nuevamente usando 'aws sso login'.")
                elif "NoCredentialsError" in str(e):
                    st.warning("No se encontraron credenciales. Ejecuta 'aws sso login' en tu terminal.")
                elif "ProfileNotFound" in str(e):
                    st.warning(f"El perfil '{sso_profile}' no existe en tu configuración de AWS.")

if __name__ == "__main__":
    test_bedrock_connection()