import os
from groq import Groq
from datetime import datetime

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
        "The assistant name is Lumin. You should respond truthfully, avoiding human-like lies or deceit. "
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
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=1000,
        temperature=1.2
    )

    # Extract the assistant's response
    assistant_response = response.choices[0].message.content

    # Append the response to the chat history
    chat_history.append({"role": "assistant", "content": assistant_response})

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"TIME: {current_time}")

    # Print the response
    print("Assistant:", assistant_response)

    # Write the prompt, response, and current time to response.txt
    with open("response.txt", "a") as file:
        file.write(f"TIME: {current_time}\n")
        file.write("USER: " + user_input + "\n")
        file.write("ASSISTANT: " + assistant_response + "\n")