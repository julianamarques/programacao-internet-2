from django.db import models

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True, default='')
    release_date = models.CharField(max_length=255, blank=True, default='')
    game_category = models.CharField(max_length=255, null=True, blank=True)
    played = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ("name",)
    