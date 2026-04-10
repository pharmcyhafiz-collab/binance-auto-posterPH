import os
import random
import requests

DEEPSEEK_KEY = os.environ["DEEPSEEK_API_KEY"]
BINANCE_KEY = os.environ["BINANCE_API_KEY"]

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
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": f"Write a short engaging Binance Square post about: {topic}. Keep it under 150 words. Friendly tone. Add 3 hashtags at the end. No markdown."
            }
        ]
    }
    r = requests.post("https://api.deepseek.com/chat/completions", json=payload, headers=headers)
    result = r.json()
    return result["choices"][0]["message"]["content"]

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
print("Done!")import os
import random
import requests

DEEPSEEK_KEY = os.environ["DEEPSEEK_API_KEY"]
BINANCE_KEY = os.environ["BINANCE_API_KEY"]

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
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": f"Write a short engaging Binance Square post about: {topic}. Keep it under 150 words. Friendly tone. Add 3 hashtags at the end. No markdown."
            }
        ]
    }
    r = requests.post("https://api.deepseek.com/chat/completions", json=payload, headers=headers)
    result = r.json()
    return result["choices"][0]["message"]["content"]

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
