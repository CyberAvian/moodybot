import discord
import os
import logging
import random
import moods

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
        logging.info(f"{trigger} found in {message_content}")
        response_num = random.randint(0, len(triggers)-1)
        
        # The hello trigger does not generate a song
        if trigger == 'hello':
          logging.info(f"{trigger} does not have a song")
          response = triggers[trigger][response_num]
        else:
          logging.info(f"Fetching {trigger} song")
          song_info = moods.convert_song_to_string(trigger)
          response = f"{triggers[trigger][response_num]}\n\n{song_info}"

        await message.channel.send(response)
        return
      else:
        logging.info(f"{trigger} not found in {message_content}")
    
    logging.info("Did not find any triggers.")
    await message.channel.send("I do not understand the response. Please try again.")
  else:
    logging.info(f"{message_content} does not start with moody,")
    return

client.run(moody_token)