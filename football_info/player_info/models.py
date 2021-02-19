from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth = models.DateField()
    info = models.TextField()
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
