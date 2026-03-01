import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()
    user_prompt = args.user_prompt
    verbose = args.verbose
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("environment variable wasn't found")
    print("Hello from bd-ai-agent!")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash"
    messages = types.Content(role="user", parts=[types.Part(text=user_prompt)])
    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    function_calls = response.function_calls
    usage_metadata = response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("there is a problem with request")
    prompt_token_count = usage_metadata.prompt_token_count
    candidates_token_count = usage_metadata.candidates_token_count
    # if verbose:
    #     print(
    #         f"User prompt: {user_prompt}",
    #         f"Prompt tokens: {prompt_token_count}",
    #         f"Response tokens: {candidates_token_count}",
    #         f"Response:",
    #         response.text,
    #         sep="\n",
    #     )
    # else:
    #     print(
    #         f"Response:",
    #         response.text,
    #         sep="\n",
    #     )
    if len(function_calls):
        for call in function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(
            f"Response:",
            response.text,
            sep="\n",
        )


if __name__ == "__main__":
    main()
