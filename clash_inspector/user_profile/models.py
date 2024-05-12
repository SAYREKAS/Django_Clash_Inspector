from django.contrib.auth.models import User
from django.db import models


class UserProfile(User):
    player_tag = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Профіль гравця'
        verbose_name_plural = 'Профілі гравців'
