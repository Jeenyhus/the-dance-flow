from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

class Dancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Instructor, related_name='dancers')

class DanceStudio(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Instructor)
    name = models.CharField(max_length=255)
    subscription_fee = models.DecimalField(max_digits=10, decimal_places=2)
    premium_fee = models.DecimalField(max_digits=10, decimal_places=2)
    basic_fee = models.DecimalField(max_digits=10, decimal_places=2)
    subscribers = models.ManyToManyField(Dancer, related_name='subscribed_studios')

class Subscription(models.Model):
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    studio = models.ForeignKey(DanceStudio, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)