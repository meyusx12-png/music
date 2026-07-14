import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

app = Client(
    "MeyusMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

user = Client(
    "MeyusAssistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

call_py = PyTgCalls(user)

def main():
    print("🎵 Meyus Music VC başlatılıyor...")

    app.start()
    user.start()
    call_py.start()

    print("✅ Meyus Music VC aktif!")

    idle()

    call_py.stop()
    user.stop()
    app.stop()

if __name__ == "__main__":
    main()