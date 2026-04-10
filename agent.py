import os
import random
import requests
from google import genai

GEMINI_KEY = os.environ["GEMINI_API_KEY"]
BINANCE_KEY = os.environ["BINANCE_API_KEY"]

client = genai.Client(api_key=GEMINI_KEY)

TOPICS = [
    "Bitcoin latest price movement",
    "Why crypto is the future of money",
    "Top 3 altcoins to watch this week",
    "What is DeFi and how does it work",
    "BNB Chain advantages explained",
    "Crypto trading tips for beginners",
    "Why blockchain technology matters",
]

def make_post():
    topic = random.choice(TOPICS)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Write a short engaging Binance Square post about: {topic}. Keep it under 150 words. Friendly tone. Add 3 hashtags at the end. No markdown."
    )
    return response.text

def publish(content):
    url = "https://www.binance.com/bapi/social/v1/friendly/social/post/create"
    headers = {"X-MBX-APIKEY": BINANCE_KEY, "Content-Type": "application/json"}
    r = requests.post(url, json={"content": content}, headers=headers)
    print("Status:", r.status_code)
    print("Response:", r.text)

print("Generating post...")
post = make_post()
print("Post content:\n", post)
publish(post)
print("Done!")
