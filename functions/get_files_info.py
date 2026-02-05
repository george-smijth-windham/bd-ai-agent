import os


def get_files_info(working_directory, directory="."):
    abs_work_path = os.path.abspath(working_directory)
    print(abs_work_path)


get_files_info("calculator")
