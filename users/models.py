import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=False, null=False)
    mobile_number = models.CharField(max_length=15, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    referral_code = models.CharField(max_length=100, blank=True, null=True)
    referrer_code = models.CharField(max_length=100, unique=True)
    
    REQUIRED_FIELDS = ['name', 'mobile_number','city'] 
    
    def save(self, *args, **kwargs):
        if not self.referrer_code:
            self.referrer_code = str(uuid.uuid4())[:6]  # Generates an random 6-character code for refferal.
        super().save(*args, **kwargs)  # Calls the parent class's save method
