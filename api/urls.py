from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('get/', views.get, name='get'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
