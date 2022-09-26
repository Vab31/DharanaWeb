from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from django.utils.timezone import now

class pageinfo(models.Model):
    page_id=models.IntegerField(AutoField,primary_key=True);
    thumbnail=models.ImageField(null=True,blank=True);
    logo= models.ImageField(null=True,blank=True);
    title=models.CharField(max_length=50,null=True);
    subscriber=models.IntegerField();
    content1=models.CharField(max_length=2000,null=True)
    content2=models.CharField(max_length=2000,null=True)

# Create your models here.
class review(models.Model):
    # id=models.ForeignKey(pageinfo,on_delete=models.CASCADE,primary_key=True)
    comment=models.CharField(max_length=1000, unique=True ,null=True);
    type=models.CharField(max_length=120,null=False)
    username= models.ForeignKey(User,on_delete=models.CASCADE, null=True);
    # email= models.ForeignKey(User,on_delete=models.CASCADE, null=True);
    email= models.CharField(max_length=70,null=True);
    timeStamp=models.DateTimeField(default=now)
    
class rating(models.Model):
    # id=models.ForeignKey(pageinfo,on_delete=models.CASCADE,primary_key=True)
    rate=models.IntegerField(null=True);
    type=models.CharField(max_length=120,null=False)
    # username= models.ForeignKey(User,on_delete=models.CASCADE,null=True);
    email= models.CharField(max_length=70,null=True);
    timeStamp=models.DateTimeField(default=now)

class languagerating(models.Model):
    # id=models.ForeignKey(pageinfo,on_delete=models.CASCADE,primary_key=True)
    rate=models.IntegerField();
    type=models.CharField(max_length=120,null=False)
    # username= models.ForeignKey(User,on_delete=models.CASCADE,null=True);
    email= models.CharField(max_length=70,null=True);
    timeStamp=models.DateTimeField(default=now)

class interactionrating(models.Model):
    # id=models.ForeignKey(pageinfo,on_delete=models.CASCADE,primary_key=True)
    rate=models.IntegerField();
    email= models.CharField(max_length=50,null=True);
    type=models.CharField(max_length=120,null=False);
    # username= models.ForeignKey(User,on_delete=models.CASCADE,null=True);
    
    timeStamp=models.DateTimeField(default=now)



class qualityrating(models.Model):
    # id=models.ForeignKey(pageinfo,on_delete=models.CASCADE,primary_key=True)
    rate=models.IntegerField();
    type=models.CharField(max_length=120,null=False)
    # username= models.ForeignKey(User,on_delete=models.CASCADE,null=True);
    email= models.CharField(max_length=50,null=True);
    timeStamp=models.DateTimeField(default=now)

# class user_detai(models.Model):
#   username=models.CharField(max_length=50);
#   email=models.CharField(max_length=50)
#   password=models.CharField( max_length=50)
    
class Info(models.Model):
  email=models.CharField(max_length=50, null=True, unique='true');
  comment=models.CharField(max_length=1000, null=True);



