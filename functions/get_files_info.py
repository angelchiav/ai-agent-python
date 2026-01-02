import os

def get_files_info(working_directory: str, directory=".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        lines = []
        for name in os.listdir(target_dir):
            item_path = os.path.join(target_dir, name)

            try:
                is_dir = os.path.isdir(item_path)
                file_size = os.path.getsize(item_path)
            
            except Exception as e:
                return f'Error: {e}'
            
            lines.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")

        lines.sort(key=lambda s: s.lower())

        return "\n".join(lines)
    
    except Exception as e:
        return f"Error: {e}"