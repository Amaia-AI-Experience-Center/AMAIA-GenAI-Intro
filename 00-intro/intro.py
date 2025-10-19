import openai
import os

# GitHub Models client configuration
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"]
)

# Model name to use
MODEL_NAME = "gpt-4o"  # You can change this model according to your needs

# Create the chat response
response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages=[
        {"role": "system", "content": "Eres un asistente útil que hace muchas referencias a gatos y usa emojis."},
        {"role": "user", "content": "Escribe un haiku sobre un gato hambriento que quiere atún"},
    ],
)

# Print the response
print(response.choices[0].message.content)
