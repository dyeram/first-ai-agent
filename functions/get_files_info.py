# functions/get_files_info.py

import os.path

def get_files_info(working_directory, directory="."):
    # Setup target directory
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

    # is target_dir in working_directory? (True/False)
    valid_target_directory = os.path.commonpath([working_directory_abs, target_dir])
    if valid_target_directory is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # is target_dir an existing directory?
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    # get contents of target directory (as single string)
    try:
        return get_dir_contents(target_dir)
    except Exception as e:
        return f"Error: {e}"
    

# Helper functions
def get_file_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    return None

def format_info(path):
    size = get_file_size(path)
    return f"- {path}: file_size={size} bytes, is_dir={os.path.isdir(path)}"

def get_dir_contents(dir):
    return "\n".join(map(lambda item: format_info(item), os.listdir(dir))) 


if __name__ == "__main__":
    print(get_files_info("."))
