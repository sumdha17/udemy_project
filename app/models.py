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
    
    
    
class Testimonial(models.Model):
    stars_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        
    ]
    user_image = models.CharField(max_length=255, blank=True, null=True)
    rating_count = models.IntegerField(choices=stars_count)
    username = models.CharField(max_length=100)
    user_job_title = models.CharField(max_length=100)
    review = models.TextField()
    
    def __str__(self):
        return self.user_job_title    
    
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_msg = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.email




class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
class Blog(models.Model):
    blog_image = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, blank=True,  max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title