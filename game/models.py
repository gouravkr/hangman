from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WordMaster(models.Model):
    category_choices = [
        ('movies', 'Movies'),
        ('celebrities', 'Celebreties'),
        ('places', 'Places')
    ]
    word = models.CharField("Secret Word", max_length=100)
    category = models.CharField("Category", max_length=20, choices=category_choices)
    sub_category = models.CharField("Sub-category", max_length=50)
    last_used = models.DateTimeField("Last used", auto_now=False, auto_now_add=False, null=True)
    used_count = models.DateTimeField("Used count", auto_now=False, auto_now_add=False, null=True)
    correct_guesses = models.IntegerField("Correct guesses", null=True)

class GamesPlayed(models.Model):
    word_master = models.ForeignKey(WordMaster, on_delete=models.DO_NOTHING)
    guessed_letters = models.CharField("Guessed letters", max_length=72, null=True)
    guesses = models.IntegerField("Number of guesses", null=True)
    won = models.BooleanField("Won", null=True)
    start_time = models.DateTimeField("Started", auto_now=True, auto_now_add=False, null=True)
    end_time = models.DateTimeField("Ended", auto_now=False, auto_now_add=True, null=True)
    feedback = models.IntegerField("Feedback", null=True)
