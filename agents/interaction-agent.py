import discord
from discord.ext import commands

class InteractionAgent:

    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = commands.Bot(command_prefix='!')

    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

    def run(self):
        self.bot.run(self.bot_token)

if __name__ == '__main__':
    bot_token = 'your-discord-bot-token'  # replace this with your Discord bot token
    agent = InteractionAgent(bot_token)
    agent.run()
