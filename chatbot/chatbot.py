from together import Together

# Initialize Together AI client
together_client = Together(api_key="e3ab4476326269947afb85e9c0b0ed5fe9ae2949e27ed3a38ee4913d8f807b3e")

def get_chatbot_response(user_message):
    """Send user input to Together AI and return response."""
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Always format your responses in HTML. Use <ul> for bullet points and <li> for each point. Keep answers short and clear."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=699,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
    )
    
    return response.choices[0].message.content
