import os
import openai

# GitHub Models client configuration
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"]
)

# Model name to use
MODEL_NAME = os.getenv("GITHUB_MODEL", "openai/gpt-4o")


response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[{"role": "user", "content": "Explica cómo funcionan los LLM en un solo párrafo."}],
)

explanation = response.choices[0].message.content
print("Explicación: ", explanation)
response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {
            "role": "user",
            "content": (
                "Eres un editor. Revisa la explicación y proporciona comentarios detallados sobre claridad, coherencia "
                "y cautivación (pero no la edites tú mismo):\n\n"
            )
            + explanation,
        }
    ],
)

feedback = response.choices[0].message.content
print("\n\nRetroalimentación: ", feedback)

response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {
            "role": "user",
            "content": (
                "Revisa el artículo utilizando los siguientes comentarios, pero mantenlo a un solo párrafo."
                f"\nExplicación:\n{explanation}\n\nComentarios:\n{feedback}"
            ),
        }
    ],
)

final_article = response.choices[0].message.content
print("\n\nFinal Article: ", final_article)
