from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='api'
urlpatterns = [
    path('users/', views.add_user_view, name='add_user'),
    re_path(r'^users/(?P<username>\w{0,50})$', views.delete_user_view, name='delete_user'),
    path('categories/', views.add_category_view, name='add_category'),
    path('categories/<slug:category_name>/',views.delete_category_view, name='delete_category'),
    #path('categories/<slug:category_name>/acts/',views.get_category_act_view,name='list_act_category'),
    path('categories/<slug:category_name>/acts/',views.list_act_in_category,name='list_act_in_category'),
    path('categories/<slug:category_name>/acts/size/',views.list_num_acts_category,name='list_of_acts_per_category'),
    path('acts/upvote/',views.upvote_act,name='upvote_act'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
