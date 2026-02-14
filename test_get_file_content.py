from functions.get_file_content import get_file_content
from config import MAX_CHARS

file_content = get_file_content("calculator", "lorem.txt")

if len(file_content) >= MAX_CHARS:
    print(f"{file_content[MAX_CHARS:]}\n")

print(
    get_file_content("calculator", "main.py"),
    get_file_content("calculator", "pkg/calculator.py"),
    get_file_content("calculator", "/bin/cat"),
    get_file_content("calculator", "pkg/does_not_exist.py"),
    sep="\n",
)
