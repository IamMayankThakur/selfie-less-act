from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='api'
urlpatterns = [
    path('acts/<int:act_id>', views.remove_act,name='remove_act'),
    path('categories', views.add_category_view, name='add_category'),
    path('categories/<slug:category_name>',views.delete_category_view, name='delete_category'),
    path('categories/<slug:category_name>/acts',views.get_category_act_view,name='list_act_category'),
    path('categories/<slug:category_name>/acts/size',views.list_num_acts_category,name='list_of_acts_per_category'),
    path('acts/upvote',views.upvote_act,name='upvote_act'),
    path('acts', views.upload_an_act, name='upload_an_act'),
    path('count', views.CountActsView.as_view(), name="Count no of acts"),
    path('_count', views.CountView.as_view(), name="Count/Reset api count"),
    path('_health', views.HealthView.as_view(), name="Check health"),
    path('_crash', views.CrashView.as_view(), name="Crash all apis"),
    path('_resetcrash', views.ResetCrashView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
