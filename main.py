import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


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
    )
    usage_metadata = response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("there is a problem with request")
    prompt_token_count = usage_metadata.prompt_token_count
    candidates_token_count = usage_metadata.candidates_token_count
    if verbose:
        print(
            f"User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            f"Prompt tokens: {prompt_token_count}",
            f"Response tokens: {candidates_token_count}",
            f"Response:",
            response.text,
            sep="\n",
        )
    else:
        print(
            f"Response:",
            response.text,
            sep="\n",
        )


if __name__ == "__main__":
    main()
