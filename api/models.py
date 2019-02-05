from django.db import models

# Create your models here.
# Category: (catId, categoryName)
# Act: (actId, url, upvote, timestamp, caption, category)

class Category(models.Model):
	category_name = models.CharField(max_length=128, unique=True)
	def __str__(self):
		return self.category_name

class Act(models.Model):
	image = models.ImageField()
	upvote = models.IntegerField()
	timestamp = models.DateTimeField(auto_now=True)
	caption = models.CharField(max_length=512)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)


