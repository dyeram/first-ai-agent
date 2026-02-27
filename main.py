import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description = 'AI chatbot')
    parser.add_argument("user_prompt", type = str, help = "User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Load API key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
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
            tools=[available_functions],
        ),
    )

    # Verify successful API request
    if not response.usage_metadata:
        raise RuntimeError("API request failed")
    
    # Print --verbose response
    if verbose:
        print(f"User prompt: {prompt}")
        # print(f"System prompt: {system_prompt}") 
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # Execute function call(s)
    if response.function_calls is not None:

        all_parts = [] # list to store function_call_result.parts[0]

        for function_call in response.function_calls:
            
            # Call the function and save the result
            function_call_result = call_function(function_call, verbose=verbose) # returns a Content object

            # Check that the result is valid
            if not function_call_result.parts:
                raise ValueError("Content.parts must not be empty (returned empty list)")
            if function_call_result.parts[0].function_response is None:
                raise ValueError("FunctionResponse must not be empty (returned None)")
            if function_call_result.parts[0].function_response.response is None:
                raise ValueError("FunctionResponse.response must not be empty (returned None)")
            
            all_parts.append(function_call_result.parts[0])

            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    else: 
        # Print response: text (default response)
        print(f"Response: {response.text}")
    

if __name__ == "__main__":
    main()
