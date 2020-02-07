from django.urls import path
from . import views

urlpatterns = [
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.home, name='home'),
  path('campgo/', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('camp_create/', views.CampsiteCreate.as_view(), name='camp_create'),
  path('camp_edit/<int:campsite_id>/', views.camp_edit, name='camp_edit'),
  path('camp_delete/', views.camp_delete, name='camp_delete'),
  path('camp_show/<int:campsite_id>/', views.camp_show, name='camp_show'),
  path('favlist/', views.fav_list, name="favlist")
]
