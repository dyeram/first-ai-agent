# functions/write_file.py

import os.path
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        # Setup target_file_path
        abs_working_directory = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        # is target_file_path in working_directory? (True/False)
        valid_target_file = os.path.commonpath([abs_working_directory, target_file_path]) == abs_working_directory
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # is target_file_path an existing directory?
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Create all parent directories of target_file_path (if they dont exist already)
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"
    

# Declaration: provides schema which tells LLM how to call the function
# Security risk: DO NOT include "working_directory" inside properties!!
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=(
        "Creates or overwrites the specified file with the provided content." 
        "Automatically creates any missing parent directories."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The path of the specified file that is being written to. "
                    "The file's parent directories are also created if they do not exist already. "
                    "The file's path is relative to the working directory"
                ),
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file."
            )
        },
        required=["file_path", "content"],
    ),
)
