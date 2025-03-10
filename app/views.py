from django.shortcuts import render, redirect
from .models import (GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, 
ContactFormLog, Blog, Author)
# Create your views here.
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    
    blogs = Blog.objects.all().order_by("-created_at")[:3]
    
    # for i in blogs:
    #     # print(i)
    #     print(i.title)
    #     print(i.author)
    #     print(f" {i.author.last_name}")
     
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
        "blogs" : blogs,
    }
    return render(request, "index.html", context)
    
    
    
def contact_form(request):
    if request.method == 'POST':
        print("\nUser has submit a contact form\n")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        context = {
            "name" : name,
            "email" : email,
            "subject": subject,
            "message":message
        }
        html_content = render_to_string('email.html', context)
        
        is_success = False
        is_error = False
        error_msg = ""
        try:
            send_mail(
                subject=subject, 
                message=None,
                html_message= html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
        except Exception as e:
            is_error = True
            error_msg = str(e)
            messages.error(request, "Could not Send Email...")
            # print(f"email sending is failed...")
        else:
            is_error=True
            messages.success(request, "Message Send Successfully")
            
        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success = is_success,
            is_error=is_error,
            error_msg = error_msg,
            
        )
            # print("email send successfully....!")
    return redirect('index')


def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.all().exclude(id=pk).order_by("-created_at")[:2]
    
    context = {
        "blog" : blog,
        "blogs" : blogs,
        
    }
    return render(request, "blog_details.html", context)


def blogs(request):
    all_blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(all_blogs, 1)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs= paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
        
    context = {
        "blogs" : blogs,
    }
    return render(request, "blogs.html", context)