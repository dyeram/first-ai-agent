# File Management Agent

AI agent that can safely interact with a local file system using a restricted set of of tool/function calls.  
Designed as a minimal example for building LLM agents with restricted file access.

The agent is called via API queries and can perform basic function-calling logic using Google's Gemini 2.5 Flash model.

While tool access is constrained, the agent can write and execute arbitrary Python code via exposed functions. As a result, it should be treated as having developer-level access within the execution environment rather than as a fully sandboxed or secure system.

## AI Agent

- **LLM model:** Gemini 2.5 Flash

## Functions / Tools

- **File Information** – List files, subdirectories, and metadata within a specified directory  
- **Read Access** – Retrieve the contents of specific files  
- **Write Access** – Create or overwrite files, automatically creating required subdirectories  
- **Run Python File** – Execute a Python script with optional arguments  

## Security

- All file operations are restricted to a system-defined `working_directory` and its subdirectories.
- Executed code is not sandboxed and may access the broader file system. 

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/dyeram/first-ai-agent.git
cd first-ai-agent
```

### 2. Install dependencies

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
uv sync
```

### 3. Create environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

You can obtain an API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Run the agent

```bash
uv run main.py
```
