import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt

load_dotenv()

parser = argparse.ArgumentParser(description="chatbot")
parser.add_argument("user_prompt", type=str, help="user prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if args.verbose:
    print(f'User prompt: {args.user_prompt}\n')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(f'Response:\n{response.text}')

else:
    print(f'Response:\n{response.text}')