from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# models.CASCADE barcha tegishli productlar uchib ketadi
# models.DO_NOTHING  hchnarsa o'zgarmidi
# models.PROTECT  barcha tegishli productlar o'chmaguncha kategoriya o'chmidi
# ---
# ForeignKey
# OneToOneField
# ManyToManyField
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title