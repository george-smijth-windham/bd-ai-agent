from functions.get_files_info import get_files_info

working_dir = "calculator"
target_dirs = [".", "pkg", "/bin", "../"]

for target_dir in target_dirs:
    dir_name = f"'{target_dir}'" if target_dir != "." else "current"
    info = get_files_info(working_dir, target_dir)
    result = "\n  ".join([f"Result for {dir_name} directory:"] + info.split("\n"))
    print(result)
