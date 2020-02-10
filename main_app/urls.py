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
  path('camp_show/<int:campsite_id>/add_fav/', views.add_fav, name='add_fav'),
  path('favlist/<int:user_id>/', views.fav_list, name='favlist'),
  path('campgo/<int:campsite_id>/add_comment/', views.add_comment, name='add_comment'),
  path('comments/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
  path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
