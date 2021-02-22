from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    info = models.TextField()
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=25, default='-Гость-')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


class ProfileViewing(models.Model):
    ip = models.GenericIPAddressField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
