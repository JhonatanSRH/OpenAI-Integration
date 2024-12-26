"""openai module"""
# FastAPI
from fastapi import HTTPException
# OpenAI
from openai import OpenAI
# Settings
from app.config.settings import settings


CONTEXT: str = ("Tú eres un experto en evaluación de riesgos laborales, el cual, " +
                "deberá responder preguntas acerca de riesgos laborales " +
                "de la forma más seria y profesional posible.")
client = OpenAI(
    api_key=settings.openai_api_key
)

def send_message(message: str) -> str:
    """Envia un mensaje a OpenAI

    Args:
        message (str): mensaje a enviar

    Returns:
        str: respuesta de OpenAI
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "developer", "content": CONTEXT},
                {"role": "user", "content": message}
            ],
            temperature=0.8,
            max_tokens=200,
            top_p=1
        )
    except Exception as error:
        raise HTTPException(status_code=400,
                            detail=f"Error al enviar mensaje a OpenAI: {error}")
    return completion.choices[0].message

def check_openai_status() -> bool:
    """Comprueba el estado de OpenAI

    Returns:
        bool: True si OpenAI esta disponible, False en caso contrario
    """
    try:
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "ping"}
            ],
            max_tokens=10
        )
    except Exception:
        return False
    return True
