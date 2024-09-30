import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import os
from groq import Groq

# Initialize Groq client with API key from environment variable
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=api_key)

# Function to get a response from Groq
def get_ai_response(user_input):
    try:
        response = client.ask_question(user_input)  # Replace with the correct method
        return response['answer']
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle user input and display the conversation
def handle_input():
    user_input = input_text.get()
    if user_input:
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the AI assistant's response
        assistant_response = get_ai_response(user_input)

        # Append the conversation to the chat display
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"TIME: {current_time}\n")
        chat_display.insert(tk.END, f"USER: {user_input}\n")
        chat_display.insert(tk.END, f"ASSISTANT: {assistant_response}\n\n")
        chat_display.config(state=tk.DISABLED)

        # Write the conversation to response.txt
        with open("response.txt", "a") as file:
            file.write(f"TIME: {current_time}\n")
            file.write(f"USER: {user_input}\n")
            file.write(f"ASSISTANT: {assistant_response}\n\n")

        # Clear the input field
        input_text.set("")

# Initialize the main window
root = tk.Tk()
root.title("AI Chat Assistant")

# Create a scrolled text widget for displaying the chat history
chat_display = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for user input
input_text = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_text)
input_entry.pack(padx=10, pady=10, fill=tk.X)

# Create a button to submit the user input
submit_button = tk.Button(root, text="Send", command=handle_input)
submit_button.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()