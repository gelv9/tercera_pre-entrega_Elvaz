from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='infoextra')
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    
@receiver(post_save, sender=User)
def crear_info_extra(sender, instance, created, **kwargs):
    if created:
        InfoExtra.objects.create(user=instance)