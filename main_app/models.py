from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Campsite(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=1000)
  description = models.TextField()
  img_url = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  favlist = models.ManyToManyField(User, related_name="favoritor")

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('index')

class Comment(models.Model):
  content = models.TextField()
  campsite = models.ForeignKey(Campsite, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.content

  def get_absolute_url(self):
    return reverse('camp_show', kwargs={'campsite_id': self.campsite.id})