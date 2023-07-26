from django.db import models

class hero(models.Model):
    tittle = models.CharField(max_length=255,blank=True,null=True)
class facts(models.Model):
    paragraph = models.TextField(default='Lorem ipsum')
class socialplatform(models.Model):
    tittle = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return f"fact {self.id}" 
   
   
