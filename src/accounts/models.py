from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
  GIVE_DONATOR = 1
  RECIVE_DONATOR = 2
  ROLE_CHOICES ={
    (GIVE_DONATOR,'g_donate'),
    (RECIVE_DONATOR,'r_donate'),
  }
  user  = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=30, blank=True)
  nid = models.CharField(max_length=30, blank=True)
  bank = models.CharField(max_length=30, blank=True)
  birthdate = models.DateField(null=True, blank=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

  def __str__(self):  # __unicode__ for Python 2
    return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()