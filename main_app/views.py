from django.shortcuts import render, redirect
# from .models import Campsite, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'campgo/index.html')

def camp_create(request):
  return render(request, 'campgo/new.html')

def camp_edit(request):
  return render(request, 'campgo/edit.html')

def camp_delete(request):
  return render(request, 'campgo/confirm.html')

def camp_show(request):
  return render(request, 'campgo/show.html')