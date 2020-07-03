import random
import datetime

from django.db import connection
from .models import WordMaster, GamesPlayed


def start_game(category='movie'):
    words = WordMaster.objects.filter(category=category)
    word = random.choice(words)
    g = GamesPlayed(word_master=word)
    g.save()
    display = display_name(g)
    return {'id':g.id, 'status': 'Started', 'string': display}


def guess_letter(game_id, guess):
    guess = guess.lower()
    gp = GamesPlayed.objects.select_related('word_master').get(pk=game_id)

    guessed_letters = [] if gp.guessed_letters is None else gp.guessed_letters.split(',')
    guesses = 0 if gp.guesses is None else gp.guesses

    if guess in guessed_letters:
        display = display_name(gp)
        return {'id': game_id, 'status': 'duplicate', 'string': display, 'guesses': 7-guesses}
    else:
        guessed_letters.append(guess)

    if guess in gp.word_master.word:
        gp.guessed_letters = ','.join(guessed_letters)
        display = display_name(gp)
        if '_' not in display:
            gp.won = True
            status = 'won'
        else:
            status = 'correct'
    else:
        guesses += 1
        gp.guessed_letters = ','.join(guessed_letters)
        gp.guesses = guesses
        if guesses == 7:
            gp.won = False
            status = 'lost'
            display = gp.word_master.word
        else:
            display = display_name(gp)
            status = 'incorrect'
    gp.save()
    return {'id': game_id, 'status': status, 'string': display, 'guesses': 7-guesses}


def display_name(game):
    display_name = []

    word = game.word_master.word
    if game.guessed_letters is not None:
        guessed_letters = game.guessed_letters.split(',')
    else:
        guessed_letters = []
    for i in list(word):
        if i == " ":
            display_name.append(" / ")
        elif i in guessed_letters:
            display_name.append(i)
        else:
            display_name.append("_")
    display = " ".join(display_name)
    return display
