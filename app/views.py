from django.shortcuts import render
from .models import GeneralInfo, Service
# Create your views here.
from django.db import connection

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
    print(first_record)
    
    services = Service.objects.all()
    
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
    }
    return render(request, "index.html", context)
    


 