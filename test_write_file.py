from functions.write_file import write_file

def main():
    # Test cases (working directory, file_label, file_path, content)
    test_cases = [
        ("calculator", "'lorem.txt'", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "'pkg/morelorem.txt'", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "'/tmp/temp.txt'", "/tmp/temp.txt", "this should not be allowed")
    ]
    
    # loop through test cases
    for working_directory, file_label, file_path, content in test_cases:
        print(f"Result for {file_label}:")
        print(f"{write_file(working_directory, file_path, content)}")

if __name__ == "__main__":
    main()