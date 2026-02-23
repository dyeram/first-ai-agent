# functions/get_files_info.py

import os.path

def get_files_info(working_directory, directory="."):
    try:
        # Setup target directory
        abs_working_directory = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))

        # is target_dir in working_directory? (True/False)
        valid_target_directory = os.path.commonpath([abs_working_directory, target_dir]) == abs_working_directory
        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # is target_dir an existing directory?
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # get contents of target directory (as single string)
        return get_dir_contents(target_dir)
    
    except Exception as e:
        return f"Error: {e}"
    

# Helper functions
def format_info(path, item):
    size = os.path.getsize(path)
    return f"- {item}: file_size={size} bytes, is_dir={os.path.isdir(path)}"

def get_dir_contents(dir):
    return "\n".join(map(lambda item: format_info(os.path.join(dir, item), item), os.listdir(dir))) 
