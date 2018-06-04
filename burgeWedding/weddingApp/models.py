from django.db import models
from django.urls import reverse

# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=200)
    partySize = models.IntegerField()
    partyNames = models.TextField()
    allergy = models.TextField(blank=True)
    speacialRequest = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weddingApp:thanks')
