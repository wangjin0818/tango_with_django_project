from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	# For Python 2, use __str__ on Python 3
	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	# For Python 2, use __str__ on Python 3
	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance
	# User object located at django.contrib.auth.model.User
	user = models.OneToOneField(User)

	# The additional attributes we wish to include
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful
	# change submit
	def __unicode__(self):
		return self.user.username