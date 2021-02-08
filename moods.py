import random

def random_happy_song():
    dont_stop_believin = "4bHsxqR3GMrXTxEPLuK5ue"
    cant_stop_this_feelin = "1WkMMavIMc4JZ8cfMmxHkI"
    uptown_funk = "32OlwWuMpZ6b0aN2RZOeMS"
    september = "2grjqo0Frpf2okIBiifQKs"
    stargazing = "0Zbbxnx4SGGHoIow4PpISP"

    happy_songs = [dont_stop_believin,cant_stop_this_feelin,uptown_funk,september]

    return random.choice(happy_songs)

def random_sad_song():
    lonely = "4y4spB9m0Q6026KfkAvy9Q"
    stay_with_me = "5Nm9ERjJZ5oyfXZTECKmRt"
    say_you_wont_let_go = "5uCax9HTNlzGybIStD3vDh"

    sad_songs = [lonely,stay_with_me,say_you_wont_let_go]

    return random.choice(sad_songs)

def random_angry_song():
    popular_monster = "4GssB27iJeqmfGxS94Tfij"
    bow_down = "5qD3Qv8Wu3r5uRD0DahcZy"
    running_w_scissors = "6HjkNCwInDttzD7jZcbBFz"

    angry_songs = [popular_monster,bow_down,running_w_scissors]

    return random.choice(angry_songs)


def get_random_mood_song(mood = ''):
    pass


def display_mood_song(mood = "".lower()):
    link = "https://open.spotify.com/track/"
    
    if mood == "happy":
        print("Moody: Here's a happy song to make you even happier!!😃\n" + link + random_happy_song() +"\n")

    elif mood == "sad":
        print("Moody: I'm sorry your sad, here's a sad song. 😢\n" + link + random_sad_song() +"\n")

    elif mood == "angry":
        print("Moody: I'm angry because your angry! Here's a angry song 😡\n" + link + random_angry_song() +"\n")

    else:
        print("Moody doesn't know that mood yet, Try a different keyword.")

display_mood_song('happy')