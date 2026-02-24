import os
import argparse

from dotenv import load_dotenv
from prompts import system_prompt

from google import genai
from google.genai import types

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description = 'AI chatbot')
    parser.add_argument("user_prompt", type = str, help = "User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Load API key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environmental variable is missing.")
    
    # Define inputs and call LLM (via Google's genai)
    client = genai.Client(api_key = api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, messages, args.user_prompt, args.verbose)


# Generate LLM response (via Google's genai)
def generate_content(client, messages, prompt, verbose):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.5
        )
    )

    # Verify successful API request
    if response.usage_metadata is None:
        raise RuntimeError("API request failed")
    
    # Print --verbose response
    if verbose is True:
        print(f"User prompt: {prompt}")
        print(f"System prompt: {system_prompt}") 
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.prompt_token_count}")
    
    # Print response
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
