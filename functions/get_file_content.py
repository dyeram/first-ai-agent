# functions/get_file_content

import os.path
from config import CHAR_LIMIT

def get_file_content(working_directory, file_path):
    try:
        # Setup target_file_path
        abs_working_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))

        # is file_path in working_directory? (True/False)
        valid_target_file = os.path.commonpath([abs_working_directory, target_file]) == abs_working_directory
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # is file_path a file?
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # get contents of target file (as single string up to CHAR_LIMIT)
        with open(target_file, "r") as f:
            content = f.read(CHAR_LIMIT)
            
                # If there's a character at CHAR_LIMIT + 1
            if f.read(1):
                    content += f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'
            
        return content
    
    except Exception as e:
        return f"Error: {e}"
