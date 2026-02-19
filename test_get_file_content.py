from functions.get_file_content import get_file_content

def main():
    # Test cases ("working directory", "file_label", "file")
    test_cases = [
        ("calculator", "'lorem.txt'", "lorem.txt")
        # ("calculator", "'pkg'", "pkg"),
        # ("calculator", "'/bin'", "/bin"),
        # ("calculator", "'../'", "../")
    ]

    # loop through test cases
    for working_directory, file_label, file in test_cases:
        length, content = get_file_content(working_directory, file)
        print(f"Result for {file_label}:")
        print(f"Length: {length}\n")
        print(f"{content}\n")

if __name__ == "__main__":
    main()