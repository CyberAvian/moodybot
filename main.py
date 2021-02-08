import discord
import os
import logging
import random

client = discord.Client()
moody_token = os.getenv("MOODY_TOKEN")
logging.basicConfig(level=logging.INFO)

triggers = {
    "hello": ["Hello! How are you feeling today?", "Hi! Welcome to the server!", "Greetings! It is nice to see you today!"],
    "sad": ["I'm sorry to hear that. Here is a mellow track!", "Here's a track to suit your mood.", "May this track brighten your day!"],
    "happy": ["That's wonderful! Here is an upbeat track!", "I'm happy to hear that! Here's a track to suit your mood!", "May this track bring you joy!"]
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
        response_num = random.randint(0, len(triggers)-1)
        logging.info(f"{trigger} found in {message_content}")
        await message.channel.send(triggers[trigger][response_num])
        return
      else:
        logging.info(f"{trigger} not found in {message_content}")
    logging.info("Did not find any triggers.")
    await message.channel.send("I do not understand the response. Please try again.")
  else:
    return

client.run(moody_token)