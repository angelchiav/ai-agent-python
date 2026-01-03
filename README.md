# AI Agent Python

A powerful AI-powered code assistant built with Google's Gemini API that can autonomously interact with your codebase through function calling. This agent can read files, write files, list directories, and execute Python scripts within a secure, sandboxed working directory.

## Features

- **AI-Powered Code Assistance**: Leverages Google's Gemini 2.5 Flash model for intelligent code understanding and generation
- **File System Operations**: Read, write, and list files and directories
- **Python Execution**: Execute Python scripts with optional command-line arguments
- **Security-First Design**: All operations are restricted to a configurable working directory
- **Iterative Function Calling**: Supports multi-step operations through automatic function calling
- **Verbose Mode**: Optional detailed logging for debugging and monitoring

## Prerequisites

- Python >= 3.14
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/angelchiav/ai-agent-python>
cd ai-agent-python
```

2. Install dependencies using `uv` (recommended) or `pip`:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

3. Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```

## Configuration

Edit `config.py` to customize the agent's behavior:

- `MAX_CHARS`: Maximum characters to read from a file (default: 10,000)
- `WORKING_DIRECTORY`: Directory where the agent can operate (default: `./calculator`)
- `MAX_ITERS`: Maximum number of iterations for function calling (default: 20)

## Usage

### Basic Usage

Run the agent with a natural language prompt:

```bash
python main.py "List all files in the current directory"
```

### Verbose Mode

Enable verbose output to see detailed function calls and token usage:

```bash
python main.py "Read the main.py file" --verbose
```

### Examples

**List files in a directory:**
```bash
python main.py "Show me all files in the calculator directory"
```

**Read a file:**
```bash
python main.py "Read the contents of calculator/main.py"
```

**Write a file:**
```bash
python main.py "Create a new file called test.py with a hello world function"
```

**Execute a Python script:**
```bash
python main.py "Run the calculator/main.py file"
```

**Complex multi-step operations:**
```bash
python main.py "Read calculator/main.py, understand it, and create a test file for it"
```

## Available Functions

The agent has access to the following functions:

### `get_files_info`
Lists files and directories in a specified directory, providing file size and directory status.

**Parameters:**
- `directory` (optional): Directory path relative to working directory (default: ".")

### `get_file_content`
Reads the contents of a file (up to `MAX_CHARS` characters).

**Parameters:**
- `file_path` (required): Path to the file relative to the working directory

### `write_file`
Writes or overwrites a file, creating parent directories if needed.

**Parameters:**
- `file_path` (required): Path to the file relative to the working directory
- `content` (required): Content to write to the file

### `run_python_file`
Executes a Python file with optional command-line arguments and returns captured output.

**Parameters:**
- `file_path` (required): Path to the Python file relative to the working directory
- `args` (optional): List of command-line arguments to pass to the script

## Security

- **Working Directory Restriction**: All file operations are restricted to the configured working directory. The agent cannot access files outside this directory.
- **Path Validation**: All paths are validated to prevent directory traversal attacks.
- **Execution Timeout**: Python file execution has a 30-second timeout to prevent infinite loops.
- **File Size Limits**: File reading is limited to `MAX_CHARS` characters to prevent memory issues.

## Project Structure

```
ai-agent-python/
├── main.py                 # Entry point and CLI interface
├── config.py              # Configuration settings
├── prompts.py             # System prompts for the AI agent
├── generate_content.py    # Content generation and function calling logic
├── call_function.py       # Function calling dispatcher
├── functions/             # Available function implementations
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/            # Example working directory
└── pyproject.toml         # Project dependencies
```

## How It Works

1. **User Input**: The user provides a natural language prompt via the command line
2. **AI Processing**: The prompt is sent to Gemini 2.5 Flash with function calling enabled
3. **Function Execution**: If the AI determines it needs to call a function, it does so automatically
4. **Iterative Loop**: Function results are fed back to the AI, which can make additional function calls
5. **Final Response**: The process continues until the AI provides a final text response or reaches `MAX_ITERS`

## Development

### Running Tests

Test files are available for each function:
- `test_get_file_content.py`
- `test_get_files_info.py`
- `test_run_python_file.py`
- `test_write_file.py`

### Adding New Functions

To add a new function:

1. Create a new file in `functions/` with your function implementation
2. Define a schema using `types.FunctionDeclaration`
3. Import and register the function in `call_function.py`
4. Add the function to `available_functions` and `function_map`

## Dependencies

- `google-genai==1.12.1`: Google Gemini API client
- `python-dotenv==1.1.0`: Environment variable management

## Support

For issues, questions, or contributions, please [open an issue](link-to-issues) or [create a pull request](link-to-prs).
