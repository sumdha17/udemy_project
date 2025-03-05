from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "name" : "Arin"
    }
    return render(request, "index.html", context)


