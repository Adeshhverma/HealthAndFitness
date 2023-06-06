from asyncio import SendfileNotAvailableError
from datetime import date
from distutils.command.upload import upload
import email
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.shortcuts import reverse

class Contact(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=45,null=False)
    your_query=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self) :# is used to represent an object into string format 
        return self.name

class HealthCompaign(models.Model):
    campaign_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=100)
    organizer_name=models.CharField(max_length=45,null=False)
    date=models.DateField()
    pic_name=models.ImageField(max_length=225,upload_to="healthapp/campaign_pic",default="")
    def __str__(self) :
        return self.organizer_name



class HealthExpert(models.Model):
    user_name=models.CharField(max_length=45,primary_key=True)
    password=models.CharField(max_length=45,null=False)
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=45,null=False)
    city=models.TextField()
    address=models.TextField()
    gender = models.CharField(max_length=6,null=False)
    experttype=models.CharField(max_length=45,null=False)
    pic_name=models.FileField(max_length=100,upload_to="healthapp/Healthexpert_pic",default="")

class Patient(models.Model):
    user_name=models.CharField(max_length=45,primary_key=True)
    password=models.CharField(max_length=45,null=False)
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=45,null=False)
    address=models.TextField()

class Feedback(models.Model):
    user_name=models.ForeignKey(Patient,null=False,on_delete=models.DO_NOTHING)
    expert_name=models.CharField(max_length=45,null=False)
    feedback_text=models.TextField()
    rating=models.IntegerField()
    date=models.DateField(default=timezone.now)
class User_Message(models.Model):
    receiver_id=models.CharField(max_length=45,null=False,default=None)
    sender_id=models.CharField(max_length=45,null=False,default=None)
    subject=models.CharField(max_length=100,null=False)
    content=models.TextField(null=False)
    date=models.DateField(default=timezone.now)
    receiver_status=models.BooleanField(default=True,null=True)
    sender_status=models.BooleanField(default=True,null=True)
    # def get_absolute_url(self):
    #     return reverse('show_message',args=[(self.id)])

class Tips(models.Model):
    Username=models.ForeignKey("HealthExpert",on_delete=models.DO_NOTHING)
    Tips_contents=models.TextField(max_length=100,null=False)
    date=models.DateField(default=timezone.now)

class Expert_detail(models.Model):
    user_name=models.OneToOneField(HealthExpert,null=False,on_delete=models.DO_NOTHING)
    experience=models.CharField(max_length=45,null=False)
    skills=models.CharField(max_length=45,null=False)
    about=models.TextField(null=False)
    highest_qualification=models.CharField(max_length=45,null=False)
    status=models.CharField(max_length=45,default="not")

class BookingRequest(models.Model):
    from_date=models.DateField(verbose_name="start date",default=timezone.now)
    to_date=models.DateField(verbose_name="End date",default=timezone.now)
    user_name=models.ForeignKey(Patient,null=False,on_delete=models.DO_NOTHING)
    expert_user_name=models.CharField(max_length=45,null=False,default='abc ')
    request_date=models.DateField(default=timezone.now)
    status=models.CharField(max_length=45,default="not confirm")
    response_text=models.CharField(max_length=45, null=False,default="no response")
    user_message_text=models.CharField(max_length=45, null=False,default=" ")

class Prediction(models.Model):
    name = models.CharField(max_length=45)
    age= models.PositiveIntegerField(null=True, blank=True)
    gender=models.PositiveIntegerField(null=True, blank=True)
    hemoglobin= models.PositiveIntegerField(null=True, blank=True)
    weight= models.PositiveIntegerField(null=True, blank=True)
    diastolic_l=models.PositiveIntegerField(null=True, blank=True)
    systolic_h=models.PositiveIntegerField(null=True, blank=True)
    heartbeat= models.PositiveIntegerField(null=True, blank=True)
    predicted_value=models.CharField(max_length=100,blank=True)