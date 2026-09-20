import json
import time
import urllib.request
import urllib.parse

TOKEN = "8859220929:AAFdYVAUHzoT-fizIDs7ETk4JpEmRd99Iio"
API = f"https://api.telegram.org/bot{TOKEN}/"

def telegram(method, data=None):
    if data is None:
        data = {}

    encoded = urllib.parse.urlencode(data).encode()

    request = urllib.request.Request(
        API + method,
        data=encoded
    )

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())


def send_start(chat_id):

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "📖 ENTER THE LORE",
                    "url": "https://t.me/Clowx1"
                }
            ],
            [
                {
                    "text": "▶️ NEW GAME",
                    "url": "https://t.me/Clwkxbot?game=clowk"
                }
            ]
        ]
    }

    telegram(
        "sendMessage",
        {
            "chat_id": chat_id,
            "text": (
                "🕰️ C L O W X\n\n"
                "This clock was not built to tell time."
            ),
            "reply_markup": json.dumps(keyboard)
        }
    )


offset = 0

print("🕰️ CLOWX BOT IS RUNNING...")

while True:

    try:
        result = telegram(
            "getUpdates",
            {
                "offset": offset,
                "timeout": 30
            }
        )

        for update in result.get("result", []):

            offset = update["update_id"] + 1

            message = update.get("message")

            if not message:
                continue

            text = message.get("text", "")
            chat_id = message["chat"]["id"]

            if text.startswith("/start"):
                send_start(chat_id)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)
