from django.urls import path
from . import views

urlpatterns = [
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.home, name='home'),
  path('campgo/', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('camp_create/', views.camp_create, name='camp_create'),
  path('camp_edit/', views.camp_edit, name='camp_edit'),
  path('camp_delete/', views.camp_delete, name='camp_delete'),
  path('camp_show/<int:id>/', views.camp_show, name='camp_show'),
]
