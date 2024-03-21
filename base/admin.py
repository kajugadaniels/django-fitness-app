from django.contrib import admin
from base.models import *

class TrainerSocialAdmin(admin.TabularInline):
	model = TrainerSocial

class TrainerAdmin(admin.ModelAdmin):
	inlines = [TrainerSocialAdmin]
	list_display = ['title', 'role', 'trainer_image', 'trainer_status']

admin.site.register(Trainer, TrainerAdmin)
