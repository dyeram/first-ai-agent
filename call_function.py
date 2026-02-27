# Creates a Tool object that provides a list of functions that the LLM can use to generate a reponse.
# Requires: a FunctionDeclaration object (schema) for each function.

import copy

from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file

# Available function declarations
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
        ],
)

# Call functions
def call_function(function_call, verbose=False):
    
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    # Map functions names to their functions
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    # Function name: is always a string (avoids a type error)
    function_name = function_call.name or ""

    # If function name is missing from function map,
    # return a types.Content object that explains the error.
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Parts.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ]
        )
    
    # Argument dictionary: creates a shallow copy of function_call.args to work with
    # Creates an empty dictionary if function_call.args is None
    if function_call.args:
        args = dict(function_call.args)
    else:
        args = {}

    # Add system-defined keyword argument "working_directory" to the arguments dictionary
    # Security: LLM can only call functions within the working directory and its subdirectories
    args["working_directory"] = "./calculator"

    # Function call: calls the specified function with its keyword arguments and returns a string
    function_result = function_map[function_name](**args)

    # Return a types.Content object that describes the result of the function call
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result} # response has to be a dictionary
                )
            ]
    )

