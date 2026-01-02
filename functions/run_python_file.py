import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_path = os.path.commonpath([working_directory_abs, target_path]) == working_directory_abs
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not regular file'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:
            command.extend(args)

        completed = subprocess.run(
            command,
            cwd=working_directory_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        output_parts = []

        if completed.returncode != 0:
            output_parts.append(f"Process exited with code {completed.returncode}")

        if not completed.stdout and not completed.stderr:
            output_parts.append("No output produced")
        else:
            if completed.stdout:
                output_parts.append(f"STDOUT:\n{completed.stdout}")
            if completed.stderr:
                output_parts.append(f"STDERR:\n{completed.stderr}")

        return "\n".join(output_parts)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"