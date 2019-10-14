from django.db import models
from django.utils import timezone
# delete image too when object were deleted
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
# Create your models here.


class QuesSubject(models.Model):
	category_title = models.CharField(max_length=100)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=50, default=1)
	category_image = models.ImageField(upload_to="images/category/", default="images/sample-1.jpg", blank=True, null=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_title

class SubSeries(models.Model):
	series_title = models.CharField(max_length=100)
	series_summary = models.CharField(max_length=200)
	series_slug = models.CharField(max_length=50, default=1)
	series_image = models.ImageField(upload_to="images/series/", default="images/sample-1.jpg", blank=True, null=True)

	# series referencing category title of EssayCategory
	category_title = models.ForeignKey(QuesSubject, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = "Series"
	
	def __str__(self):
		return self.series_title

class Paper(models.Model):

	# Here name `essay` is used only for illustration purpose i.e. easy to design

	paper_title = models.CharField("Content Title", max_length=150)
	paper_published = models.DateTimeField("Date Published", default=timezone.now)
	# Only authenticated users can write new content so it refer to USER_MODEL and default is admin

	series_title = models.ForeignKey(SubSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	# catgory_title = models.ForeignKey(EssayCategory, verbose_name="Category", default=1, on_delete=models.SET_DEFAULT)
	
	paper_slug = models.CharField(max_length=50, default=1)
	def __str__(self):
		return self.paper_title
	
class Prank(models.Model):
	prank_title = models.CharField("Image Title", default="prank animal images", max_length=50)
	prank_image = models.ImageField(upload_to="images/prank/", default="images/h1.jpg", blank=True, null=True)

	def __str__(self):
		return self.prank_title

# for deleting images too whenever a object has been deleted
@receiver(post_delete, sender=Paper)
def submission_delete(sender, instance, **kwargs):
	instance.paper_image.delete(False) 

# Feedback Database, since it is open for all that's why doesn't used User as foreign key
class Feedback(models.Model):
	feedback_title = models.CharField(max_length=100)
	feedback_date = models.DateTimeField("Feedback Time", default=timezone.now)
	feedback_content = models.TextField(help_text="Share Your Ideas Here!")
	feedback_user_id = models.EmailField("Email ID")