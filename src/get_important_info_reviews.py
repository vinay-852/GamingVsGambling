import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import asyncio
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def extract_important_info_reviews(info):
    prompt = """
Your task is to analyze the provided app reviews and extract the most important information to determine the nature of the app. Focus on identifying language, sentiment, and specific details. Consider the following key aspects:

**1. Skill vs. Chance Emphasis:**
    * Identify mentions of skill, strategy, player control, learning curves, challenges, or tactical depth. Look for player progression or skill improvement.
    * Highlight reliance on luck, random number generators, or unpredictability. References to chance, odds, or potential for "big wins" or losses.
    * Note if reviews suggest a combination of skill and chance, and what the user considers to be the dominant aspect.

**2. Monetary Aspects and Incentives:**
    * Identify mentions of wagering, betting, real money transactions, deposits, withdrawals, payouts, jackpots, or losing money. Look for real-world value or virtual currencies with real-world value.
    * Note mentions of money spent on in-app purchases, such as cosmetic items. Identify comments about player rewards for game progression.

**3. User Experience and Engagement:**
    * Look for discussions on gameplay mechanics, engaging challenges, fun, entertainment, character progression, in-game achievements, tournaments, or social interactions.
    * Identify mentions of the thrill of risk, potential for large wins or losses, or addiction. Note if users mention losing money.
    * Note if users mention the game is pay-to-win or if they feel compelled to pay to progress.

**4. Contextual Language and Keywords:**
    * Identify words like "game," "level," "character," "strategy," "multiplayer," "fun," "challenge," "esports," "tournament."
    * Identify words like "casino," "bet," "wager," "lottery," "odds," "payout," "jackpot," "slots," "roulette," "poker," "blackjack," "money," "win," "lose."

**5. User Sentiment and Tone:**
    * Look for enthusiastic reviews highlighting enjoyment, challenges, and achievement.
    * Identify reviews expressing frustration about losses, addiction, or unfair odds.
    * Note reviews indicating the game is designed to encourage gambling.

**6. Other Relevant Details:**
    * Note any unusual or interesting details.
    * Identify if users think the app is predatory.

Your analysis should extract all pertinent details relevant to these points. Provide a clear and concise summary of the key information based on the user reviews.

Please extract the information from the following app reviews:
"""
    prompt_complete = prompt + str(info)
    response = await asyncio.to_thread(model.generate_content, prompt_complete)
    return response.text
