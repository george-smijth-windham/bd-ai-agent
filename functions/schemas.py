from google.genai import types

get_files_info = types.FunctionDeclaration(
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

get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read from a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING, description="File path to read from"
            )
        },
    ),
)

write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING, description="File path to write at"
            ),
            "content": types.Schema(
                type=types.Type.STRING, description="New content to write at file path"
            ),
        },
        required=["file_path", "content"],
    ),
)

run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of string arguments",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
