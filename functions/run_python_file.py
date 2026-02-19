from os import path


def run_python_file(working_directory, file_path, args=None):
    try:
        work_path = path.abspath(working_directory)
        target_path = path.normpath(path.join(work_path, file_path))
        valid_path = path.commonpath([work_path, target_path]) == work_path
        if not valid_path:
            raise Exception(
                f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            )

    except Exception as e:
        return str(e)
