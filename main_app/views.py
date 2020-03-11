from django.shortcuts import render, redirect
from .models import Campsite, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm


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
  comment_form = CommentForm
  return render(request, 'campgo/index.html', { 'campsites': campsites, 'comment_form':comment_form })

class CampsiteCreate(LoginRequiredMixin, CreateView):
  model = Campsite
  fields = ['name', 'location', 'description', 'img_url']
  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

@login_required
def camp_show(request, campsite_id):
  campsite = Campsite.objects.get(id=campsite_id)
  comment_form = CommentForm()
  return render(request, 'campgo/show.html', { 
    'campsite': campsite,
    'comment_form': comment_form
    })

class CampsiteUpdate(LoginRequiredMixin, UpdateView):
  model = Campsite
  fields = ['name', 'location', 'img_url', 'description']
  success_url="/camp_show/{campsite_id}/"

@login_required
def add_comment(request, campsite_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.campsite_id = campsite_id
    form.instance.user = request.user
    new_comment.save()
  return redirect('camp_show', campsite_id = campsite_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['content']

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url="/camp_show/{campsite_id}/"

@login_required
def fav_list(request, user_id):
  campsites = Campsite.objects.filter(favlist=request.user.id)
  return render(request, 'campgo/favlist.html', {"campsites": campsites})

@login_required
def assoc_favlist(request, campsite_id):
  Campsite.objects.get(id=campsite_id).favlist.add(request.user.id)
  return redirect('favlist', request.user.id)

@login_required
def unassoc_favlist(request, campsite_id):
  Campsite.objects.get(id=campsite_id).favlist.remove(request.user.id)
  return redirect('favlist', request.user.id)

@login_required
def search_new(request):
  return render(request, 'campgo/search_new.html')

