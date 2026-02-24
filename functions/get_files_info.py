import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    try:
        abs_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_work_dir, directory))
        valid_target_dir = (
            os.path.commonpath([abs_work_dir, target_dir]) == abs_work_dir
        )
        if not valid_target_dir:
            raise Exception(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(target_dir):
            raise Exception(f'Error: "{target_dir}" is not a directory')
        target_dir_contents = []
        for path in os.listdir(target_dir):
            name = path
            if name != "__pycache__":
                path = os.path.join(target_dir, name)
                size = os.path.getsize(path)
                is_dir = os.path.isdir(path)
                target_dir_contents.append(
                    f"- {name}: file_size={size} bytes, is_dir={is_dir}"
                )
            else:
                continue
        info = "\n".join(target_dir_contents)
        return info
    except Exception as e:
        return str(e)
