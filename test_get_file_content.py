from functions.get_file_content import get_file_content

def main():
    # Test cases ("working directory", "file_label", "file")
    test_cases = [
        ("calculator", "'lorem.txt'", "lorem.txt"),
        ("calculator", "'main.py'", "main.py"),
        ("calculator", "'pkg/calculator.py'", "pkg/calculator.py"),
        ("calculator", "'/bin/cat'", "/bin/cat"),
        ("calculator", "'pkg/does_not_exist.py'", "pkg/does_not_exist.py")
    ]

    # loop through test cases
    for working_directory, file_label, file in test_cases:
        content = get_file_content(working_directory, file)
        content_length = len(content)
        print(f"Result for {file_label}:")
        print(f"{content}\n")

if __name__ == "__main__":
    main()