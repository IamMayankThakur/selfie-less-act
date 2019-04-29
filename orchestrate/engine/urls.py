from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'engine'
urlpatterns = [
	path('<id>', views.ProxyView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
