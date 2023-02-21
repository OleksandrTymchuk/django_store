from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    description = models.TextField()
    approved_by = models.ForeignKey(User, related_name="approved_by", null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    display_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title