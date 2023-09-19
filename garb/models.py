from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

# Create your models here.
class Garbage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phoneNumber = models.IntegerField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=7, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name
