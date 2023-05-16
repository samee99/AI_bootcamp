import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == client.user:
            return

        # Forward the message to the webhook
        response = requests.post('http://localhost:5000/webhook', json={'content': message.content})

        if response.status_code != 200:
            print(f"Webhook POST failed with status {response.status_code}")

client = MyClient()
client.run('your-discord-bot-token')
