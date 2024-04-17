from django.db import models


class HeroImages(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='hero/')

    class Meta:
        verbose_name_plural = "Зображення героїв"
        verbose_name = "Зображення героїв"

    def __str__(self):
        return self.title
