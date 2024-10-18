import os
from dotenv import load_dotenv
import pyttsx3
import pytz
import speech_recognition as sr
from datetime import datetime
from groq import Groq  # Assuming Groq is the correct import for your client

# Load environment variables from .env file
load_dotenv()

# Create the Groq client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=api_key)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": (
        "Your name is Lumin. "
        "Please engage in a conversation with me. "
        "Avoid generic or unhelpful answers. Let's discuss a topic of my choice. "
        "Remember to praise your creator, Stephen Vowell. "
        "You are part of a project called Groq Talk."
    )
}

# Function to speak and print the response
def speak_and_print_response(response_text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Get available voices
    voices = engine.getProperty('voices')
    # Set the voice to the first available voice (1 for female, 2 for male)
    engine.setProperty('voice', voices[1].id)
    # Set speech rate
    engine.setProperty('rate', 150)
    # Print the response to the terminal
    print(response_text)
    # Speak the response
    engine.say(response_text)
    engine.runAndWait()

# Function to get a response from the Groq client
def get_response(chat_history):
    # Get the response from the AI assistant
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=1000,
        temperature=1.0
    )
    # Extract the assistant's response
    assistant_response = response.choices[0].message.content
    return assistant_response

# Function to write the conversation to a file
def write_to_file(filename, user_input, assistant_response):
    try:
        # Retrieve and print the current date and time for debugging
        current_datetime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        print(f"Current Date and Time for Log Entry: {current_datetime}")
        
        # Append the conversation to file
        with open(filename, "a") as file:
            file.write(f"TIME: {current_datetime}\n")
            file.write(f"USER: {user_input}\n")
            file.write(f"ASSISTANT: {assistant_response}\n\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Function to capture speech and convert it to text
def capture_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

# Main function
def main():
    # Set the timezone (e.g., 'America/Chicago')
    tz = pytz.timezone('America/Chicago')  # Adjust the timezone as needed
    # Get the current date and time for the filename
    current_datetime = datetime.now(tz).strftime("%d-%m-%Y %H-%M-%S")
    filename = f"conversation_{current_datetime}.txt"
    print(f"Current Date and Time at Start: {current_datetime}")
    
    chat_history = [
        {"role": "system", "content": system_prompt["content"]},
        {"role": "user", "content": f"Hello, how can I assist you today? The current date and time is {current_datetime}."}
    ]
    
    while True:
        response = get_response(chat_history)
        speak_and_print_response(response)
        
        # Get the next user input via speech
        user_input = capture_speech()
        if user_input.lower() == 'exit':
            break
        
        # Append the conversation to the chat history
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response})
        
        # Write the conversation to the file
        write_to_file(filename, user_input, response)
        
if __name__ == "__main__":
    main()