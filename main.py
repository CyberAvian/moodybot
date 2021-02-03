import discord
import os
import logging

client = discord.Client()
moody_token = os.getenv("MOODY_TOKEN")
logging.basicConfig(level=logging.INFO)

triggers = {
    "hello": ["Hello! How are you feeling today?"],
    "sad": ["I'm sorry to hear that. Here is a mellow track!"],
    "happy": ["That's wonderful! Here is an upbeat track!"]
}

@client.event
async def on_ready():
  print("Hello! I am ready to recommend music!")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message_content = message.content.lower()
  logging.info(f"Message: {message_content}")
  if message_content.startswith("moody,"):
    for trigger in triggers:
      logging.info(f"Trigger: {trigger}")
      if trigger in message_content:
        logging.info(f"{trigger} found in {message_content}")
        await message.channel.send(triggers[trigger][0])
        return
      else:
        logging.info(f"{trigger} not found in {message_content}")
    logging.info("Did not find any triggers.")
    await message.channel.send("I do not understand the response. Please try again.")
  else:
    return

client.run(moody_token)