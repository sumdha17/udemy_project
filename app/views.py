from django.shortcuts import render, redirect
from .models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion
# Create your views here.
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings

def write_sql_que_to_file(file_path):
    with open(file_path, 'w') as file:
        queries = connection.queries
        for query in queries:
            sql = query['sql']
            file.write(f"{sql}\n")

def index(request):
    # all_records = GeneralInfo.objects.all()
    # print(all_records)
    
    first_record= GeneralInfo.objects.filter().first()
    # print(first_record)
    
    services = Service.objects.all()
    
    testimonials = Testimonial.objects.all()
    
    ques = FrequentlyAskedQuestion.objects.all()
    
    file_path = 'sql_queries.log'
    write_sql_que_to_file(file_path)
    
    context = {
        "company_name": first_record.company_name,
        "location" : first_record.location,
        "phone" : first_record.phone,
        "email" : first_record.email, 
        "video_url": first_record.video_url,
        "open_hours"  :first_record.open_hours,
        
        "services" : services,
        "testimonials" : testimonials,
        "ques" : ques,
    }
    return render(request, "index.html", context)
    
    
    
def contact_form(request):
    if request.method == 'POST':
        print("\nUser has submit a contact form\n")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject=subject, 
            message=f"{name}- {message}",  
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        
    return redirect('index')


 