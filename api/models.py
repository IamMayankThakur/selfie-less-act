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
	username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	image = models.ImageField(null=True)
	upvote = models.IntegerField()
	timestamp = models.DateTimeField(auto_now=True)
	caption = models.CharField(max_length=512)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)



