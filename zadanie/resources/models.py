from django.db import models


class Resources(models.Model):
    title = models.CharField(max_length=32)
    amount = models.IntegerField()
    unit = models.CharField(max_length=32)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
