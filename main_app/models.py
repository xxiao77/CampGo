from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Campsite(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  description = models.TextField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('index')
