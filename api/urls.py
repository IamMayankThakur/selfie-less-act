from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='api'
urlpatterns = [
    path('users/', views.add_user_view, name='add_user'),
    path('acts/<int:act_id>/', views.remove_act,name='remove_act'),
    # path('acts/',views.upload_an_act, name='upload_an_act'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
