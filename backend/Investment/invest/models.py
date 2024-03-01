from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Model For the contact form
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):

        return self.name


# model to create a wallet for each user 
class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bonus=models.IntegerField()
    invested=models.IntegerField()

    def __str__(self):

        return self.user.username



#model that lets client to invest directly 
class Invest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20, decimal_places=2,null=True,default=0.00)

    def __str__(self):

        return self.user.username
