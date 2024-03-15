from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users/images/")
    mobile_no =models.CharField(max_length =30)
    class Meta:
         verbose_name = 'Custom User'
         verbose_name_plural = 'Custom User'
    
    def __str__(self) -> str:
        return self.user.first_name