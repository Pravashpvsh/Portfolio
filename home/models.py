from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    hero_img =models.ImageField(blank=True,null=True)


class socialplatform(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    facebook_link = models.CharField(max_length=255,blank=True,null=True)
    instagram_link = models.CharField(max_length=255,blank=True,null=True)
    tiktok_link = models.CharField(max_length=255,blank=True,null=True)
    linkedin_link = models.CharField(max_length=255,blank=True,null=True)
    youtube_link = models.CharField(max_length=255,blank=True,null=True)
    
class Client(models.Model):
    description = models.CharField(max_length=255,blank=True,null=True)
    happyclient = models.IntegerField(blank=True,null=True)
    project = models.IntegerField(blank=True,null=True)
    awards = models.IntegerField(blank=True,null=True)
    hoursupport = models.IntegerField(blank=True,null=True)
    display = models.BooleanField(default=True)
    