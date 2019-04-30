from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'engine'
urlpatterns = [
	re_path(r'.*', views.ProxyView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
