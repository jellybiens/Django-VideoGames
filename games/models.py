from django.db import models
from django.urls import reverse

class Console(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)

    def get_absolute_url(self):
        return reverse('games:console_games', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' - ' + self.publisher


class Game(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=35)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('games:game_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name + ' - ' + self.year
