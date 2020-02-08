from django.shortcuts import render, redirect
from .models import Campsite, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
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
  comment_form = CommentForm()
  return render(request, 'campgo/show.html', { 
    'campsite': campsite,
    'comment_form': comment_form
    })

@login_required
def camp_edit(request, campsite_id):
  return render(request, 'campgo/edit.html')

@login_required
def camp_delete(request):
  return render(request, 'campgo/confirm.html')

def add_comment(request, campsite_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.campsite_id = campsite_id
    form.instance.user = request.user
    new_comment.save()
  return redirect('camp_show', campsite_id = campsite_id)

@login_required
def fav_list(request):
<<<<<<< HEAD
  favs = Campsite.objects.filter(user=request.user)
  return render(request, 'campgo/main_app/favlist.html', { 'favs': favs })
def camp_show(request):
  return render(request, 'campgo/show.html')

# comment views
@login_required
def assoc_comments(request, campsite_id, comment_id):
  Campsite.objects.get(id=campsite_id).comments.add(comment_id)
  return redirect('detail', campsite_id=campsite_id)

@login_required
def unassoc_comments(request, campsite_id, comment_id):
  Campsite.objects.get(id=campsite_id).comments.remove(comment_id)
  return redirect('detail', campsite_id=campsite_id)

class CommentDetail(LoginRequiredMixin, DetailView):
  model = Comment

# class CommentCreate(LoginRequiredMixin, CreateView):
#   model = Comment
#   fields = '__all__'

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = []

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/comments/'
=======
  user = request.user
  campsites = []
  for campsite in Campsite.objects.all():
    if user in campsite.users:
      campsites.append(campsite)
    else:
      pass
  return render(
    request,
    'campgo/main_app/favlist.html',
    { 'campsites': campsites }
  )
>>>>>>> ryan
