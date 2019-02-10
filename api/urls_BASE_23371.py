from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='api'
urlpatterns = [
    path('users/', views.add_user_view, name='add_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)