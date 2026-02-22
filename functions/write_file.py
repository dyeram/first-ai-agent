# functions/write_file.py

import os.path

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