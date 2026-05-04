import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
API_KEY = os.getenv("GROQ_API_KEY")

def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        # Check if request succeeded
        if response.status_code != 200:
            print("Groq API Error:", response.text)
            return '{"summary": "AI error", "key_issue": "API failed", "impact": "Unknown"}'

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("Exception:", e)
        return '{"summary": "AI unavailable", "key_issue": "Exception", "impact": "Unknown"}'