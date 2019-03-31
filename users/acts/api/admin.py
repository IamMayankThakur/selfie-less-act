from django.contrib import admin
from .models import Category, Act, Count
# Register your models here.

admin.site.register(Category)
admin.site.register(Act)
admin.register(Count)
