from django.db import models

class Film(models.Model):
    judul = models.CharField(max_length=25)
    tahun = models.IntegerField()

    def __str__(self):
        return self.judul

class Gambar(models.Model):
    gambar = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.gambar.name