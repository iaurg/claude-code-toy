import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1] if len(sys.argv) > 1 else None

if not user_prompt:
    print("Please provide a text input as a command line argument.")
    sys.exit(1)

verbose_mode = "--verbose" in sys.argv

messages = [
    types.Content(
        role="user",
        parts=[types.Part(text=user_prompt)],
    )
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
)

if verbose_mode:
    print('User prompt:', user_prompt)
    print('Prompt tokens:', response.usage_metadata.prompt_token_count)
    print('Response tokens:', response.usage_metadata.candidates_token_count)