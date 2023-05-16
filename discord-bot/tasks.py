from celery import Celery

# initialize Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')

# define a task that sends a message to a Discord channel
@app.task
def send_discord_message(channel_id, message_content):
    import discord

    # create a discord.Client instance
    client = discord.Client()

    # define what the bot should do when it has connected to Discord
    @client.event
    async def on_ready():
        # get the channel
        channel = client.get_channel(channel_id)

        # send the message
        await channel.send(message_content)

        # close the connection
        await client.close()

    # run the bot
    client.run('your-discord-bot-token')

# define a task that gets the content of a message
@app.task
def get_message_content(message_id):
    import discord

    # create a discord.Client instance
    client = discord.Client()

    # define what the bot should do when it has connected to Discord
    @client.event
    async def on_ready():
        # get the message
        message = await client.fetch_message(message_id)

        # print the message content
        print(message.content)

        # close the connection
        await client.close()

    # run the bot
    client.run('your-discord-bot-token')
