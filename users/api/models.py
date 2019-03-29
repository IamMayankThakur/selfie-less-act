from django.db import models
from django.contrib.auth.models import User

class Count(models.Model):
	api_count = models.IntegerField(default=0)

	def __str__(self):
		return self.api_count