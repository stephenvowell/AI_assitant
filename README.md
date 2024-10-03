# Groq Search

This project provides a script to read and filter responses from a log file based on a specified date and interact with the Groq AI assistant to get answers to user questions.

## Prerequisites

- Python 3.6 or higher
- Groq API key

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/groq-search.git
   cd groq-search

```markdown
# Groq Search

This project provides a script to read and filter responses from a log file based on a specified date and interact with the Groq AI assistant to get answers to user questions.

## Prerequisites

- Python 3.6 or higher
- Groq API key

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/groq-search.git
   cd groq-search
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set the `GROQ_API_KEY` environment variable with your Groq API key:
   ```sh
   export GROQ_API_KEY=your_api_key_here  # On Linux/Mac
   set GROQ_API_KEY=your_api_key_here     # On Windows
   ```

## Usage

1. Ensure you have a `response.txt` file in the same directory as the script. This file should contain conversation logs with timestamps, user inputs, and assistant responses in the following format:
   ```
   TIME: 2023-10-01 12:00:00
   USER: What is the status of the project?
   ASSISTANT: The project is on track and will be completed by the end of the month.
   ```

2. Run the script:
   ```sh
   python groq-Search.py
   ```

3. Follow the prompts to enter a date and a question. The script will filter the responses from the log file based on the entered date and get the AI's answer to the question based on the filtered responses.

## Example

```sh
Please enter the date (YYYY-MM-DD HH:MM:SS) or type 'exit' to quit: 2023-10-01 00:00:00
Please enter your question: What did the assistant say about the project?
AI Answer: The project is on track and will be completed by the end of the month.
```

## Code Explanation

### Imports and Initialization

```python
import os
from datetime import datetime
from groq import Groq  # Assuming Groq is the correct import for your client

# Create the Groq client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")
client = Groq(api_key=api_key)
```

- **Imports necessary modules**:
  - [`os`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition"): For accessing environment variables.
  - [`datetime`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition"): For date and time manipulation.
  - [`Groq`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A17%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition"): For interacting with the Groq API.
- **

Creates

 the Groq client**:
  - Retrieves the Groq API key from the environment variable [`GROQ_API_KEY`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A26%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition").
  - Raises an error if the API key is not set.
  - Initializes the Groq client with the API key.

### Reading and Filtering Responses

```python
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
```

- **Function [`read_and_filter_responses`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A4%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition")**:
  - Reads and filters responses from a file based on a specified date.
  - Converts the date string to a [`datetime`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition") object for comparison.
  - Iterates through each line in the file, extracting the date, user input, and assistant response.
  - Filters responses that are on or after the specified date and appends them to the [`filtered_responses`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A11%2C%22character%22%3A4%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition") list.

### Getting Response from AI

```python
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
```

- **Function [`get_response_from_ai`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FAI_assitant%2Fgroq-Search.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A45%2C%22character%22%3A4%7D%7D%5D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "Go to definition")**:
  - Constructs a chat history with the context and question.
  - Sends the chat history to the Groq API to get the assistant's response.
  - Returns the assistant's response.

### Main Function

```python
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
```

- **Main Function**:
  - Prompts the user to enter a date and a question.
  - Validates the date format.
  - Reads and filters responses from the [`response.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FAI_assitant%2Fresponse.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%222e6df135-e283-4eba-ba38-4008b97d1e36%22%5D "d:\AI_assitant\response.txt") file based on the entered date.
  - Constructs the context from the filtered responses.
  - Gets the AI's answer to the question based on the context.
  - Continues to prompt the user until they type 'exit'.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact vowellstephen@gmail.com
```

This `README.md` file provides a comprehensive overview of the project, including installation instructions, usage examples, and a detailed explanation of the code.
