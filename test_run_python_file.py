from functions.run_python_file import run_python_file

def main():
    # Test cases [working_direcotory, file_label, "arg_label", "file_path", "arg"]
    test_cases = [
        ("calculator", "main.py", None),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py", None),
        ("calculator", "../main.py", None),
        ("calculator", "nonexistent.py", None),
        ("calculator", "lorem.txt", None)
    ]

    # loop through test cases
    for working_directory, file_path, args in test_cases:
        print(f"Result for '{file_path}' | args={args}")
        print(f"{run_python_file(working_directory, file_path, args=None)}")

if __name__ == "__main__":
    main()