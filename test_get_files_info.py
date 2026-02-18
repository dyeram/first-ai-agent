from functions.get_files_info import get_files_info

def main():
    # Test cases ("working directory", "directory_label", "directory")
    test_cases = [
        ("calculator", "current directory", "."),
        ("calculator", "'pkg'", "pkg"),
        ("calculator", "'/bin'", "/bin"),
        ("calculator", "'../'", "../")
    ]

    # loop through test cases
    for working_directory, directory_label, directory in test_cases:
        print(f"Result for {directory_label}:")
        print(f"{get_files_info(working_directory, directory)}\n")

if __name__ == "__main__":
    main()