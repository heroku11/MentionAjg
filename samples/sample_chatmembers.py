# -*- coding: utf-8 -*-

"""
- Tag Para Member / admin bangsat
"""

import creds
from pyrogram import Client, Filters

app = Client(creds.token, api_id=creds.id, api_hash=creds.hash)


@app.on_message(Filters.command(["members"]))
def calla(client, message):
    print("channel id:", message.chat.id)
    participants = app.get_chat_members(chat_id=message.chat.id, offset=0, limit=200)
    client.send_message(message.chat.id, "Participants: " + str(participants))


app.run()
