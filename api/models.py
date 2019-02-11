from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Category: (catId, categoryName)
# Act: (actId, url, upvote, timestamp, caption, category)

class Category(models.Model):
	category_name = models.CharField(max_length=128, unique=True)
	def __str__(self):
		return self.category_name

class Act(models.Model):
	actId = models.IntegerField(blank=True, default=0)
	username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	image = models.ImageField(blank=True, default=None)
	upvote = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=True)
	caption = models.CharField(max_length=512)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)



