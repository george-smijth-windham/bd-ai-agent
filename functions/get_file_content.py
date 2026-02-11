import os

MAX_CHARS = 5


def get_file_content(working_directory, file_path):
    try:
        abs_work_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_work_dir, file_path))
        valid_target_file = (
            os.path.commonpath([abs_work_dir, target_file]) == abs_work_dir
        )
        if not valid_target_file:
            raise Exception(
                f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(target_file):
            raise Exception(
                f'Error: File not found or is not a regular file: "{file_path}"'
            )
        # print(abs_work_dir, target_file, sep="\n")
        # return
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            file_content_overflow = f.read(5)
            if file_content_overflow:
                print("there is more content")
            else:
                print("file is under or at max chars")
    except Exception as e:
        return str(e)


print(get_file_content("calculator", "lorem.txt"))
