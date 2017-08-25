import datetime 
import calendar
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

#A user's profile is created/updated each time a user is created/updated 
class Profile(models.Model):
	'''
	A user's profile is created/updated each time a user is created/updated 
	'''
	user= models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


#Product items are linked to users through their profile
class ProductItem (models.Model):
	'''
	An element of the product tree
	'''
	product_item_name = models.CharField(max_length=200, default='Unnamed')
	product_tree_number = models.IntegerField(default=0)
	subsystem_code = models.CharField(max_length=200, null=True)
	description = models.TextField(null=True)
	team_member = models.ManyToManyField(Profile)
	sub_system = models.ManyToManyField('self',blank=True, symmetrical=False)
		
	PHASE_CHOICE= (
		('ITT','ITT Phase'),
		('DEV', 'DevelopmentPhase'),
		('H/W','H/W Phase'),
		('QUA','Quality Review'),
	)

	phase = models.CharField(
		max_length =3,
		choices=PHASE_CHOICE,
		default='ITT',
	)

	def __str__(self):
		return self.product_item_name	

	def save(self, *args, **kwargs): 
		'''
		Create a group for each product item
		'''
		item_group=Group.objects.create(name=self.product_item_name)
		for profile in self.team_member.all():
			item_group.user_set.add(profile.user)
		super().save(*args, **kwargs)  # Call the "real" save() method.

class Event (models.Model):#Can have several occurences
	event_name = models.CharField(max_length=200, default='Unnamed') 
	product_item = models.ForeignKey('ProductItem')
	TYPE_CHOICE= (
		('TELC','Telecon'),
		('REV', 'Review'),
		('MEET','Meeting'),
		('TEST','Test'),
	)

	event_type = models.CharField(
		max_length =4,
		choices=TYPE_CHOICE,
		default='Meeting',
	)
	def __str__(self):
		return self.event_name

class Occurence(models.Model):
	occurence_name = models.CharField(max_length=200, default='Unnamed')
	event = models.ForeignKey('Event')
	attendee=models.ManyToManyField(Profile)
	start_time = models.DateTimeField(default=timezone.now()+datetime.timedelta(days=7))
	duration = models.DurationField(default = datetime.timedelta(hours=2))
	all_day = models.BooleanField(default=False)
	def __str__(self):
		return self.occurence_name		

class Task (models.Model):
	task_name = models.CharField(max_length=200, default='Unnamed')
	due_date = models.DateTimeField(default=timezone.now()+datetime.timedelta(days=7))
	description = models.TextField(null=True)
	product_item = models.ForeignKey('ProductItem')
	responsable = models.ForeignKey('Profile', null='True')
	def __str__(self):
		return self.task_name











