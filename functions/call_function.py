from google.genai import types
from functions.schemas import (
    get_files_info as get_files_info_schema,
    get_file_content as get_file_content_schema,
    write_file as write_file_schema,
    run_python_file as run_python_file_schema,
)
from functions.get_files_info import get_files_info as fn_get_files_info
from functions.get_file_content import get_file_content as fn_get_file_content
from functions.write_file import write_file as fn_write_file
from functions.run_python_file import run_python_file as fn_run_python_file


available_functions = types.Tool(
    function_declarations=[
        get_files_info_schema,
        get_file_content_schema,
        write_file_schema,
        run_python_file_schema,
    ]
)

function_map = {
    "get_files_info": fn_get_files_info,
    "get_file_content": fn_get_file_content,
    "write_file": fn_write_file,
    "run_python_file": fn_run_python_file,
}


def call_function(function_call, verbose=False):
    if not verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
    function_name = function_call.name if function_call.name else ""
    function_args = dict(function_call.args) if function_call.args else {}
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    else:
        function_args["working_directory"] = "./calculator"
        function_result = function_map[function_name](**function_args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
