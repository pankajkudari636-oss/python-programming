import ollama

def ask_ai(question):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "Answer briefly in 1-2 sentences. Be fast and direct."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]