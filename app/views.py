from django.shortcuts import render,redirect
from .import models
from .scraper import scrape_website
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'blogs':models.BolgPost.objects.all()
    }
    return render(request,'index.html',context)



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(name = name , email = email , subject = subject , message = message)
        messages.success(request, 'Thank You for Your Contact us')
        return redirect('index')
    return render(request,'contact.html')



def scrap(request):
    data = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        data = scrape_website(url=url)
    return render(request, 'scrap.html', {'data': data})