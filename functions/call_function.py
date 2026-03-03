from google.genai import types
from functions.schemas import get_files_info, get_file_content

available_functions = types.Tool(
    function_declarations=[get_files_info, get_file_content]
)
