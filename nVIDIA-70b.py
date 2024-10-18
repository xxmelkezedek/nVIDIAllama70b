from openai import OpenAI

def obter_input_usuario():
    return input("Digite sua pergunta para o assistente: ")

def gerar_resposta(pergunta):
    client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = "API_KEY_HERE"
    )

    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":pergunta}
        ],
        temperature=0.5,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )

    print("Resposta do assistente:")
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print("\n")  # Adiciona uma linha em branco no final da resposta

# Uso das funções
pergunta_usuario = obter_input_usuario()
gerar_resposta(pergunta_usuario)