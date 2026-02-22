import os
import threading
import discord
from flask import Flask

# Flask app for UptimeRobot pings
app = Flask(__name__)

@app.route('/')
def home():
    return 'Online', 200

@app.route('/ping')
def ping():
    return 'Pong', 200

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Connected as {client.user}')

def main():
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print('Error: DISCORD_TOKEN environment variable not set')
        return

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    client.run(token, bot=False)

if __name__ == '__main__':
    main()
