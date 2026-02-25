# Creates a Tool object that provides a list of functions that the LLM can use to generate a reponse.
# Requires: a FunctionDeclaration object (schema) for each function.

from google.genai import types

from functions.get_files_info import schema_get_files_info

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)