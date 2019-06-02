from django.db import models
# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

# Create your models here.

class Campaign(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(blank= True)
    image = models.ImageField(upload_to='images/', blank=True)
    iname = models.CharField(max_length=200)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True)
    isPublic = models.NullBooleanField()

    def __str__(self):
        return self.title
#Campaign.objects.filter(user=logged_in_user)
