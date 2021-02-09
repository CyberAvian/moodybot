import random
import  json

# Gets a random song by Mood
def get_song(mood = ''):
    random_song = []

    # Opens songs.json
    with open('./songs.json') as json_file:
        data = json.load(json_file)

        # Displays the songs recieved from json
        for i in data['Songs']:
            # If the songs match the mood,
            # it adds to a empty list
            if i['mood'] == mood.capitalize():
                random_song.append(i)

        # Returns a random song from list
        return random.choice(random_song)