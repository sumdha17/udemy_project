from django.contrib import admin
from app.models import (GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, 
Blog, Author)
# Register your models here.
admin.site.register(GeneralInfo)
admin.site.register(Service)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(ContactFormLog)
admin.site.register(Blog)
admin.site.register(Author)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "user_job_title",
        "display_rating_count"
    ]
    
    def display_rating_count(self, obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description = "Rating"