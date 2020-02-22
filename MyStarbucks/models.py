from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class new_view(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image')
    content = models.CharField(max_length=225)


class guestbook(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)


class Detail_drink(models.Model):
    title = models.CharField(max_length=225)
    image = models.CharField(max_length=255)
    price = models.FloatField()


class CartInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Detail_drink, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)  # 买的数量
