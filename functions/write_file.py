from os import path


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
        return ("continue", target_path)
    except Exception as e:
        return str(e)


print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
