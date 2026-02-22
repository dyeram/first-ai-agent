# functions/write_file.py

import os.path

def write_file(working_directory, file_path, content):
    try:
        # Setup target_file_path
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))

        # is target_file_path in working_directory? (True/False)
        valid_target_file = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # is target_file_path an existing directory?
        if not os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Create all parent directories of target_file_path (if they dont exist already)
        target_file_path = os.makedirs(target_file_path, exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"