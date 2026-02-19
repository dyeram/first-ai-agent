# functions/get_file_content

import os.path

def get_file_content(working_directory, file_path):
    # Setup target_file_path
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

    # is file_path in working_directory? (True/False)
    valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # is file_path a file?
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a directory'
