from django.urls import path
from . import views

urlpatterns = [
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.home, name='home'),
  path('campgo/', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('camp_create/', views.CampsiteCreate.as_view(), name='camp_create'),
  path('camp_update/<int:pk>/', views.CampsiteUpdate.as_view(), name='camp_update'),
  path('camp_show/<int:campsite_id>/', views.camp_show, name='camp_show'),
  path('campgo/<int:campsite_id>/assoc_favlist/<int:favlist_id>/', views.assoc_favlist, name='assoc_favlist'),
  path('campgo/<int:campsite_id>/unassoc_favlist/<int:favlist_id>/', views.unassoc_favlist, name='unassoc_favlist'),
  path('favlist/<int:user_id>/', views.fav_list, name='favlist'),
  path('campgo/<int:campsite_id>/add_comment/', views.add_comment, name='add_comment'),
  path('comments/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
  path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
  path('campgo/search/', views.search_new, name='search_new')
]
