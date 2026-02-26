# File Management Agent

This project provides a set of tools for an AI agent to safely interact with a local file system.
The AI agent is called via API queries.

## AI Agent:
- **LLM model**: Google's gemini-2.5-flash

## Functions / Tools

- **File Information**: List files, subdirectories and associated metadata within specified directory.
- **Read Access**: Retrieve the contents of specific files.
- **Write Access**: Create or overwrite specified files with new content, automatically creating necessary subdirectories.
- **Run Python file**: Execute a specified Pythin file, passing optional arguments. 

## Security

- All file operations are restricted to a specific `working_directory` and its subdirectories.
- The agent validates all paths to prevent unauthorized access to the rest of the host system.
- A 30 second timeout prevents the agent from running indefinitely.

