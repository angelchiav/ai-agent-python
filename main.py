import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt
from generate_content import generate_content
from config import MAX_ITERS

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(MAX_ITERS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f"Maximum iterations ({MAX_ITERS}) reached")
    sys.exit(1)

if __name__ == "__main__":
    main()