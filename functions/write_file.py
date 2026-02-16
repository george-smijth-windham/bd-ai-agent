from os import path, makedirs


def write_file(working_directory, file_path, content):
    try:
        abs_path = path.abspath(working_directory)
        target_path = path.normpath(path.join(abs_path, file_path))
        valid_path = path.commonpath([abs_path, target_path]) == abs_path
        if not valid_path:
            raise Exception(
                f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            )
        if path.isdir(target_path):
            raise Exception(
                f'Error: Cannot write to "{file_path}" as it is a directory'
            )
        target_dir = path.dirname(target_path)
        makedirs(target_dir, exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return str(e)
