#set GROQ_API_KEY in the secrets

import os
from groq import Groq

# Create the Groq client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=api_key)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": (
        "I'm having a conversation with an AI assistant trained on the llama3-70b-8192 model. "
        "The assistant name is Sam. you should respond truthfully, avoiding human-like lies or deceit. "
        "Please engage in a conversation with me, showcasing empathetic and nuanced responses, "
        "and avoiding generic or unhelpful answers. Let's discuss a topic of your choice or respond to my questions."
    )
}

# Initialize the chat history
chat_history = [system_prompt]

while True:
    # Get user input from the console
    user_input = input("You: ")

    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Get the response from the AI assistant
    response = client.chat(
        prompt=user_input,
        system_prompt=system_prompt
    )

    # Check if the response is valid
    if response:
        # Extract the assistant's response
        assistant_response = response["choices"][0]["message"]["content"]
        print(f"Assistant: {assistant_response}")

        # Append the assistant's response to the chat history
        chat_history.append({"role": "assistant", "content": assistant_response})

        # Write the prompt and response to response.txt
        with open("response.txt", "a") as file:
            file.write("User: " + user_input + "\n")
            file.write("Assistant: " + assistant_response + "\n")
    else:
        print("Failed to get response from API")