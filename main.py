import os
import argparse
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function
from config import MAX_ITERATIONS

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
    
    # Define inputs and LLM model (we use Google's genai)
    client = genai.Client(api_key = api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Print user prompt --verbose response
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

        
    # call the LLM model and handle reponses
    generate_content(client, messages, args.verbose)


# Generate LLM responses (via Google's genai)
def generate_content(client, messages, verbose):

    for _ in range(MAX_ITERATIONS):

        # Call LLM model and generate response    
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[available_functions],
            ),
        )

        # Print token counts --verbose response 
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        # Add all model-generated messages to the conversation history
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)

        # Verify successful API request
        if not response.usage_metadata:
            raise RuntimeError("API request failed")

        # Execute function call(s)
        if response.function_calls is not None:

            function_responses = [] # List of function result parts
            for function_call in response.function_calls:
                
                # Call the function and save the result
                function_call_result = call_function(function_call, verbose=verbose) # returns a Content object

                # Check that the result is valid
                parts = function_call_result.parts
                if not parts:
                    raise ValueError("Content.parts must not be empty (returned empty list)")
                
                part0 = parts[0] 
                fr = part0.function_response
                if fr is None:
                    raise ValueError("FunctionResponse must not be empty (returned None)")

                fr_resp = fr.response
                if fr_resp is None:            
                    raise ValueError("FunctionResponse.response must not be empty (returned None)")
                
                # Add model-generated tool result to conversation history
                messages.append(function_call_result)

                if verbose:
                    print(f"-> {fr_resp}")

                # Add function result part to list of function responses
                function_responses.append(part0)

            # Add function responses to the conversation history
            messages.append(types.Content(role="user", parts=function_responses))

        else: 
            # Print response: text (default response)
            print(f"Response: {response.text}")
            break
    
    else: 
        print("LLM model: max iterations reached without a final response.")
        sys.exit(1)
    

if __name__ == "__main__":
    main()
