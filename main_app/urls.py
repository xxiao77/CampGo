from django.urls import path
from . import views

urlpatterns = [
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.home, name='home'),
  path('campgo/', views.index, name='index'),
  path('about/', views.about, name='about'),
]
  