from google.genai import types
from schemas import get_files_info

available_functions = types.Tool(function_declarations=[get_files_info])
