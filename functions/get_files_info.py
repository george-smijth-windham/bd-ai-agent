import os


def get_files_info(working_directory, directory="."):
    abs_work_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_work_dir, directory))
    valid_target_dir = os.path.commonpath([abs_work_dir, target_dir]) == abs_work_dir
    if not valid_target_dir:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return
    if not os.path.isdir(target_dir):
        print(f'Error: "{target_dir}" is not a directory')
        return
    print(abs_work_dir, target_dir, valid_target_dir, sep="\n")


get_files_info("calculator")
