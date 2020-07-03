from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from .utils import start_game, guess_letter
# Create your views here.

def hangman(request):
    return render(request, 'home.html', {'game_name': "Let's play Hangman!"})


class PlayGame(View):

    def get(self, request):
        res = start_game()
        res.update({'guesses': 7})
        return render(request, 'home.html', res)

    def post(self, request):
        game_id = request.POST.get('game_id')
        letter = request.POST.get('letter')
        res = guess_letter(game_id, letter)
        return render(request, 'home.html', res)


class VueGame(View):

    def get(self, request):
        res = start_game()
        res.update({'guesses': 7})
        return render(request, 'game.html', res)

    def post(self, request):
        game_id = request.POST.get('game_id')
        letter = request.POST.get('letter')
        res = guess_letter(game_id, letter)
        return render(request, 'game.html', res)
