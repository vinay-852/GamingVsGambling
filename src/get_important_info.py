import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import asyncio
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def extract_important_info(info):
    prompt = """
Your task is to analyze the provided text and extract the most important information to determine whether the content is related to **gaming** or **gambling**. Your analysis should focus on identifying the following key elements:

**1. Skill vs. Chance Emphasis:**
*   **Gaming Emphasis:** Does the activity emphasize skill, strategy, practice, player input, or learning? Look for terms related to gameplay, tactics, challenges, or character progression.
*   **Gambling Emphasis:** Does the activity rely heavily on chance, random outcomes, or luck? Look for terms related to betting, odds, payouts, randomness, or jackpots. Note if RNGs (Random Number Generators) or similar mechanics are involved.
*   **Combination:** Does the activity involve a mix of skill and chance? If so, how significant is each component?

**2. Monetary Risk and Rewards:**
*   **Gambling Focus:** Does the activity involve wagering, betting, or risking real-world money (or equivalents like virtual currency or in-game items with real-world value)? Look for terms like "stakes," "betting," "winnings," "losses," or "payouts."
*   **Gaming Focus:** If money is involved, is it for cosmetic items, in-game purchases, or as a reward for skill-based accomplishments (e.g., esports tournament prizes)? Is the financial risk optional or required?
*   **Financial Value:** Does the activity focus on the potential for financial gain?

**3. Contextual Clues:**
*   **Platform:** Is the activity taking place on a known gaming platform (e.g., Steam, PSN, Twitch) or a known gambling site (e.g., online casino, betting site)?
*   **Event Type:** Is it a tournament, casual play, esports competition (gaming), or a lottery draw, casino game, sports betting event (gambling)?
*   **Terms of Service:** If available, does the content reference rules related to betting, winnings, or age restrictions?
*   **Source/Authority:** Where did this information come from? Is the source a reputable video game website or a betting website?

**4. Motivation and Purpose:**
*   **Gaming Motivation:** Is the activity primarily designed for entertainment, challenge, social interaction, or skill improvement?
*   **Gambling Motivation:** Is the activity primarily driven by the desire to win money or other rewards of real-world value?

**5. Key Terminology:**
*   **Gaming Keywords:** Look for terms like "video game," "esports," "gameplay," "strategy," "tournament," "level," "character," "skill," "multiplayer."
*   **Gambling Keywords:** Look for terms like "casino," "bet," "wager," "lottery," "odds," "payout," "jackpot," "roulette," "slots," "poker," "blackjack."

Your analysis should extract all pertinent details relevant to these points. Your response should be a clear and concise summary of the key information to classify the activity as gaming or gambling.

Please extract the information from the following text:
"""
    prompt_complete = prompt + str(info)
    response = await asyncio.to_thread(model.generate_content, prompt_complete)
    return response.text