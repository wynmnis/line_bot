import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("epvfQ1uvTHGSKUluaueWWsrD7tAphMhBXjrTJLLxhlJ2DSUG2yhm5Vs/U+6qYy8ClAIy8fsQ6+TrCZ3MWfUQ1KVWWOW3N1DKmndLdIc69dXei6Qs/ZAHIt5P15k3WHkO4i4j8/byK93qFaQbFlDliwdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("7c14af9d5f69a3ac7a84a4e6657cc364"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
