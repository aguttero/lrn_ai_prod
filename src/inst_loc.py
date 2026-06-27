from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai
from google.genai import types

app = FastAPI()
config = dotenv_values("../.env")

GEMINI_API_KEY = config.get("GEMINI_FREE_API_KEY")
# GEMINI_API_KEY = config.get("GEMINI_PREPAID_API_KEY")
print("genai api key:", GEMINI_API_KEY)


# --- Initialize the native Google Gen AI Client
# client = genai.Client(api_key=GEMINI_API_KEY)

system_prompt = ""
user_message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""


@app.get("/", response_class=HTMLResponse)
def instant():
    client = genai.Client(api_key=GEMINI_API_KEY)
    # messages = [{"role": "user", "content": user_message}]
    # chat = client.chats.create(model="gemini-2.5-flash")
    chat = client.chats.create(model="gemini-2.5-flash")
    response = chat.send_message(user_message)
    reply = response.text.replace("\n", "<br/>")

    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"

    # return "Live from production!"
    return html
