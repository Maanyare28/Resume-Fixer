import requests
from bs4 import BeautifulSoup
import openai
import pswd
from pswd import chatgptkey

# Replace with your actual OpenAI API key
API_KEY = chatgptkey

client = openai.OpenAI(api_key=API_KEY)


def get_webpage_content(url):
    """Fetch and extract text from the given URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text, or you can filter it based on tags you need
        content = soup.get_text(separator=" ", strip=True)
        return content
    except Exception as e:
        return f"Error occurred: {e}"


def chat_with_gpt(content):
    """Send the extracted content to ChatGPT for processing"""
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # Ask the user to provide the URL or some content manually
    user_input = input("Enter the URL to scrape or provide some information directly: ")

    if user_input.startswith('http'):
        # If the input is a URL, scrape the content from the webpage
        print("Fetching and processing the webpage...")
        webpage_content = get_webpage_content(user_input)

        if "Error occurred" not in webpage_content:
            print("Processing the content with ChatGPT...")
            reply = chat_with_gpt(webpage_content)
            print("ChatGPT Response:", reply)
        else:
            print(webpage_content)  # Display the error message
    else:
        # If the input is not a URL, use it directly as content
        print("Processing the provided content with ChatGPT...")
        reply = chat_with_gpt(user_input)
        print("ChatGPT Response:", reply)
