import os
import openai

# GitHub Models client configuration
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"]
)

# Model name to use
MODEL_NAME = os.getenv("GITHUB_MODEL", "openai/gpt-4o")


SYSTEM_MESSAGE = """
Eres un asistente útil que ayuda a estudiantes con sus tareas.
En lugar de proporcionar la respuesta completa, respondes con una pista o una clave.
"""


USER_MESSAGE = "¿Cuál es el planeta más grande en nuestro sistema solar?"


response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": "¿Cuál es la capital de Francia?"},
        {"role": "assistant", "content": "¿Recuerdes el nombre de la ciudad que es conocida por la Torre Eiffel?"},
        {"role": "user", "content": "¿Cuál es la raíz cuadrada de 144?"},
        {"role": "assistant", "content": "¿Qué número multiplicado por sí mismo es igual a 144?"},
        {"role": "user", "content": "¿Cuál es el número atómico del oxígeno?"},
        {"role": "assistant", "content": "¿Cuántos protones tiene un átomo de oxígeno?"},
        {"role": "user", "content": USER_MESSAGE},
    ],
)


print(f"Repuesta de {API_HOST}: \n")
print(response.choices[0].message.content)
