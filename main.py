import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("environment variable wasn't found")
    print("Hello from bd-ai-agent!")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash"
    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model=model,
        contents=user_prompt,
    )
    usage_metadata = response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("there is a problem with request")
    prompt_token_count = usage_metadata.prompt_token_count
    candidates_token_count = usage_metadata.candidates_token_count
    print(
        f"User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        f"Prompt tokens: {prompt_token_count}",
        f"Response tokens: {candidates_token_count}",
        f"Response:",
        response.text,
        sep="\n",
    )


if __name__ == "__main__":
    main()
