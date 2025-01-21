import google.generativeai as genai
from dotenv import load_dotenv
import os
import asyncio
from pydantic import BaseModel

class result(BaseModel):
    classification: str
    explaination_from_app_description: str
    explaination_from_app_permissions: str
    explaination_from_app_reviews: str

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def extract_important_gg(info):
    prompt = """
    Your task is to analyze the provided text which is related to gambling or gaming. I will give the text from analyzing the app description, reviews, and permissions. You have to identify whether the text is related to gambling or gaming. You should classify it as gambling or gaming with reasoning. The result should be context specific, don't assume anything. Gambling with real or virtual money is always gambling, remember that.
    """
    prompt_complete = prompt + str(info)
    response = await asyncio.to_thread(model.generate_content, prompt_complete,generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=result
    ))
    return response.text