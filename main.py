import os
import threading
import discord
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

client = discord.Client()

@client.event
async def on_ready():
    print(f'Connected as {client.user}')

token = os.environ.get('DISCORD_TOKEN')
if not token:
    raise ValueError('DISCORD_TOKEN environment variable is not set')

threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()
client.run(token, bot=False)
