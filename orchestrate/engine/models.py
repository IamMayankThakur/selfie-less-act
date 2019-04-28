from django.db import models

# Create your models here.


class Count(models.Model):
	api_count = models.IntegerField(default=0)

