import openai
from docutils.nodes import system_message

import pswd
from pswd import chatgptkey

# Replace with your actual OpenAI API key
API_KEY = chatgptkey

client = openai.OpenAI(api_key=API_KEY)

def chat_with_gpt(prompt):
    system_message = "Use Bing web browsing to access links and information: "

    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": system_message}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Ask ChatGPT: ")
    reply = chat_with_gpt(user_input)
    print("ChatGPT:", reply)
'''
1. Post link of job description.
2. ChatGPT reads it 
3. Then asks to upload resume
4. Then it edits resume 
* Steps 2 and 3 can be swapped.

All in a GUI
'''