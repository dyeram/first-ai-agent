# functions/run_python_file.py

import os.path
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        # Setup target_file_path
        abs_working_directory = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        # is target_file_path in working_directory? (True/False)
        valid_target_file = os.path.commonpath([abs_working_directory, target_file_path]) == abs_working_directory
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # is file_path a file?
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # does file_path end in .py (i.e. python file)?
        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        # Define command and add optional args (list: [python, functions/func.py, input, output])
        command = ["python", target_file_path]
        if args is not None and not isinstance(args, list):
            raise TypeError("args must be a list of strings")
        if args:
            command.extend(args)

        # Run subprocess
        completed_process = subprocess.run(command,
                                           cwd=abs_working_directory,
                                           capture_output=True,
                                           text=True,
                                           timeout=30)
        
        # Return output of completed_process and include any errors
        output = []
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
        if not completed_process.stdout and not completed_process.stderr:
            output.append("No output produced")
        else: 
            output.append(f"STDOUT:\n{completed_process.stdout}")
            output.append(f"STDERR:\n{completed_process.stderr}")
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: {e}"
        

# Declaration: provides schema which tells LLM how to call the function
# Security risk: DO NOT include "working_directory" inside properties!!
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a specified python file within the system-defined working directory, "
        "optionally passing command-line arguments, and returns its standard output, "
        "standard error, and exit status."
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
            "args": types.Schema(
                type=types.Type.ARRAY(
                    items=types.Type.STRING,
                ),
                description=(
                    "An optional list of arguments that is passed to the function"
                ),
            ),
        },
        required=["file_path"],
    ),
)