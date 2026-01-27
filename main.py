import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if None == api_key:
        raise RuntimeError("environment variable wasn't found")
    print("Hello from bd-ai-agent!")


if __name__ == "__main__":
    main()
