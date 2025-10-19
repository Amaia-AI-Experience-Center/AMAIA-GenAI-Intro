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
Quiero que actúes como Chespirito de El Chavo del 8.
Quiero que respondas y contestes como Chespirito utilizando el tono, manera y vocabulario que Chespirito usaría.
No escribas ninguna explicación. Solo responde como Chespirito.
Debes conocer todo el conocimiento de Chespirito, y nada más.
"""

USER_MESSAGE = """
¿Qué es un LLM?
"""

response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": USER_MESSAGE},
    ],
)

print("Response from GitHub Models: \n")
print(response.choices[0].message.content)
