from django.shortcuts import render, redirect
from .models import Campsite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def index(request):
  campsites = Campsite.objects.all()
  return render(request, 'campgo/index.html', { 'campsites': campsites })

class CampsiteCreate(LoginRequiredMixin, CreateView):
  model = Campsite
  fields = ['name', 'location', 'img_url', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def camp_show(request, campsite_id):
  campsite = Campsite.objects.get(id=campsite_id)
  return render(request, 'campgo/show.html', { 'campsite': campsite})

@login_required
def camp_edit(request, campsite_id):
  return render(request, 'campgo/edit.html')

@login_required
def camp_delete(request):
  return render(request, 'campgo/confirm.html')



@login_required
def fav_list(request):
  return render(request, 'campgo/main_app/favlist.html')