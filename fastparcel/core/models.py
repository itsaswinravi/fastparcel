from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='customer/avatars',blank=True,null=True)

    def __str__(self):
        return self.user.get_full_name()
        