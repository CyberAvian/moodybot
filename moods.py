import random
import  json

# Gets a random song by Mood
def get_song_by_mood(mood = ''):
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

def convert_song_to_string(mood = {}):
    song = []

    song_string = ""

    # Adds mood to song list
    for i in mood.keys():
        song.append(f"{i.capitalize()}: {mood[i]}\n")

    # Converts song list to string
    for s in song:      
        song_string += s

    return song_string