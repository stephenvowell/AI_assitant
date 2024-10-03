import os
from datetime import datetime
from groq import Groq  # Assuming Groq is the correct import for your client

# Create the Groq client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=api_key)

def read_and_filter_responses(file_path, date_str):
    filtered_responses = []
    current_date = None
    current_user = None
    current_assistant = None

    # Convert date_str to datetime object for comparison
    filter_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("TIME:"):
                current_date = line.split("TIME: ")[1]
            elif line.startswith("USER:"):
                if "USER: " in line:
                    current_user = line.split("USER: ")[1]
            elif line.startswith("ASSISTANT:"):
                if "ASSISTANT: " in line:
                    current_assistant = line.split("ASSISTANT: ")[1]
                if current_date and current_user and current_assistant:
                    # Convert current_date to datetime object for comparison
                    current_date_obj = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
                    if current_date_obj >= filter_date:
                        filtered_responses.append({
                            "date": current_date,
                            "user": current_user,
                            "assistant": current_assistant
                        })
                    current_date = None
                    current_user = None
                    current_assistant = None

    return filtered_responses

def get_response_from_ai(question, context):
    chat_history = [
        {"role": "system", "content": "You are an AI assistant."},
        {"role": "user", "content": f"Here is the context: {context}"},
        {"role": "user", "content": question}
    ]

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=1000,
        temperature=1.2
    )

    assistant_response = response.choices[0].message.content
    return assistant_response

def main():
    file_path = "response.txt"

    while True:
        date_str = input("Please enter the date (YYYY-MM-DD HH:MM:SS) or type 'exit' to quit: ")
        if date_str.lower() == 'exit':
            break

        # Validate date format
        try:
            datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.")
            continue

        question = input("Please enter your question: ")

        filtered_responses = read_and_filter_responses(file_path, date_str)
        context = "\n".join([f"USER: {resp['user']}\nASSISTANT: {resp['assistant']}" for resp in filtered_responses])

        if context:
            answer = get_response_from_ai(question, context)
            print(f"AI Answer: {answer}")
        else:
            print("No responses found for the given date.")

if __name__ == "__main__":
    main()    git add groq-Search.py    git add groq-Search.py