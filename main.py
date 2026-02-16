import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description = 'AI chatbot')
    parser.add_argument("user_prompt", type = str, help = "User prompt")
    args = parser.parse_args()

    # Load API key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environmental variable is missing.")
    
    # Define inputs and call LLM (via Google's genai)
    client = genai.Client(api_key = api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, messages)


# Generate LLM response (via Google's genai)
def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )

    # Verify successful API request
    if response.usage_metadata is None:
        raise RuntimeError("API request failed")
    
    # Print LLM response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.prompt_token_count}") 
    print(response.text)

if __name__ == "__main__":
    main()
