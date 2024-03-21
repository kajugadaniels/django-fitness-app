from django.db import models
from django.utils.html import mark_safe

STATUS = (
	("active", "Active"),
	("unactive", "Unactive"),
)

class Trainer(models.Model):
	title = models.CharField(max_length=100, default="John Doe")
	role = models.CharField(max_length=100, default="Lifting Trainer")
	image = models.ImageField(upload_to="trainers", default="trainer.jpg")
	trainer_status = models.CharField(choices=STATUS, max_length=10, default="active")
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Trainer"

	def trainer_image(self):
		return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

	def __str__(self):
		return self.title

class TrainerSocial(models.Model):
	instagram = models.CharField(max_length=100)
	trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)
