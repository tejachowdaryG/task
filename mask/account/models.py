from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    is_team_leader=models.BooleanField(default=False)
    is_team_members=models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)









class Team_task(models.Model):
	STATUS=(
    	('assined','assined'),
    	('progress','progress'),
    	('under review','under review'),
    	)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	tlid=models.IntegerField(null=True, blank=True)
	name=models.CharField(max_length=255, null=True, blank=True)
	team=models.CharField(max_length=255, null=True, blank=True)
	team_members=models.CharField(max_length=255, null=True, blank=True)
	status=models.CharField(max_length=255, null=True, blank=True, choices=STATUS)
	started_at=models.DateTimeField( null=True, blank=True)
	completed_at=models.DateTimeField( null=True, blank=True)
	def __str__(self):
		return self.name

class Team_model(models.Model):
	
	eid=models.IntegerField(null=True, blank=True)
	name=models.CharField(max_length=255, null=True, blank=True)
	team_leader=models.CharField(max_length=255, null=True, blank=True)
	team_members=models.CharField(max_length=255,null=True, blank=True)

