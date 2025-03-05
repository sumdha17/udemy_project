from django.db import models

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.company_name
    
    
class Service(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title