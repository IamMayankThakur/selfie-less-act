from django.contrib import admin
from .models import Category, Act, Count, Crash
# Register your models here.

admin.site.register(Category)
admin.site.register(Act)
admin.site.register(Count)
admin.site.register(Crash)
