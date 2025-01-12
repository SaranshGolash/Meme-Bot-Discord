import discord, requests, json, os
from dotenv import load_dotenv
from typing import Final
load_dotenv()
token: Final[str] = os.getenv('TOKEN')
# Getting meme via requests.get and returning the url of the meme
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']
# Responding to user messages
class MyClient(discord.Client):
    async def on_ready(self) :
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents = intents)
client.run(token)