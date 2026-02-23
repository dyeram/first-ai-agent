# functions/run_python_file.py

import os.path
import subprocess

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
        if not os.path.isfile(file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # does file_path end in .py (i.e. python file)?
        if not target_file_path.endswith(".py")
            return f'Error: "{file_path}" is not a Python file'
        
        # Define command and add optional args (list: [python, functions/func.py, input, output])
        command = ["python", target_file_path]
        if args is not None and not isinstance(args, list):
            raise TypeError("args must be a list of strings")
        if args is not None:
            command.extend(args)

        # Run subprocess
        completed_process = subprocess.run(command, cwd=abs_working_directory, capture_output=True, text=True, timeout=30):
        
        # Return output of completed_process and include any errors
        output = []
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
        if completed_process.stdout is None and completed_process.stderr is None:
            output.append("No output produced")
        else: 
            output.append(f"STDOUT:{completed_process.stdout}")
            output.append(f"STDERR:{completed_process.stderr}")
        return "\.n".join(output)
    
    except Exception as e:
        return f"Error: {e}"
        



        












    except Exception as e:
        return f"Error: {e}"