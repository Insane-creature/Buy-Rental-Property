from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"This is Anshika Soni",
        "variable2":"and I'm very sundar sundar bacha"
    }
    return render(request, "index.html",context)
    # return HttpResponse("this is home page.")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("this is about page.")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        contact = Contact(name = name,email = email, query = query, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
         

    return render(request, "contact.html")

