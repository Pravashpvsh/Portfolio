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
    description = models.TextField(blank=True,null=True)
    happyclient = models.IntegerField(blank=True,null=True)
    project = models.IntegerField(blank=True,null=True)
    awards = models.IntegerField(blank=True,null=True)
    hoursupport = models.IntegerField(blank=True,null=True)
  
class contact(models.Model):
    location =models.CharField(max_length=255,blank=True,null=True)
    email =models.EmailField(max_length=255,blank=True,null=True)
    call =models.CharField(max_length=20,blank=True, null=True)
    

class Skill(models.Model):
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    percentage = models.PositiveIntegerField(blank=True, null=True)

   
class Testimonial(models.Model):
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    person_name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Abouts(models.Model):
    photo = models.ImageField(upload_to='Abouts/', blank=True, null=True)
    title = models.CharField(max_length=255,blank=True, null=True)
    title_description =models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_freelance_available = models.BooleanField(default=False,blank=True, null=True)
