from os import path
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        work_path = path.abspath(working_directory)
        target_path = path.normpath(path.join(work_path, file_path))
        valid_path = path.commonpath([work_path, target_path]) == work_path
        _, file_ext = path.splitext(target_path)
        if not valid_path:
            raise Exception(
                f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            )
        if not path.isfile(target_path):
            raise Exception(
                f'Error: "{file_path}" does not exist or is not a regular file'
            )
        if not file_ext or file_ext != ".py":
            raise Exception(f'Error: "{file_path}" is not a Python file')
        command = ["python", target_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(command, text=True)

    except Exception as e:
        return str(e)


result = run_python_file("calculator", "main.py")
print(result)
