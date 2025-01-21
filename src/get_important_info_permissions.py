import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import asyncio
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def extract_important_info_permissions(info):
    prompt = """
Your task is to analyze the provided app permissions and extract the most important information, particularly any permissions that could be related to gambling or gaming. Do **not** classify the app as related to gambling or gaming, but highlight permissions that are commonly associated with these areas. Consider these key aspects:
1. Identify permissions that allow access to sensitive user data.
2. Highlight permissions that enable in-app purchases or financial transactions.
3. Note any permissions that allow access to location data.
4. Identify permissions that enable communication with external servers.
5. Highlight permissions that allow access to user behavior or usage patterns.
Please extract the information from the following app permissions:
"""
    prompt_complete = prompt + str(info)
    response = await asyncio.to_thread(model.generate_content, prompt_complete)
    return response.text
