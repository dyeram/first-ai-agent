# File Management Agent

This project provides a set of tools for an AI agent to safely interact with a local file system.
The AI agent is called via API queries and is capable of performing basic function calling logic.

## AI Agent
- **LLM model**: Google's gemini-2.5-flash

## Functions / Tools
- **File Information** (`get_files_info`): List files, subdirectories and associated metadata within a specified directory.
- **Read Access** (`get_file_content`): Retrieve the contents of a specific file.
- **Write Access** (`write_file`): Create or overwrite a specified file with new content, automatically creating necessary subdirectories.
- **Run Python file** (`run_python_file`): Execute a specified Python file, passing optional arguments. 

## Setup & Quick Start
1. **Install Dependencies**:
    Make sure you have [uv](https://github.com/astral-sh/uv) installed, then run:
   ```bash
   uv sync
   ```

2. **Configure Environment**:
    Add your API key to a .env file:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

3. Run the Agent:
    ```bash
    uv run main.py
    ```

## Security
- All file operations are restricted to a system-defined `working_directory` and its subdirectories.
- Path validation is enforced within the file operation functions to prevent access outside this directory.
- A 30-second timeout prevents the agent from running indefinitely (see Roadmap).
    