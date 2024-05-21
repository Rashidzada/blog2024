from django.shortcuts import render
from .import models
from .scraper import scrape_website
# Create your views here.
def index(request):
    context = {
        'blogs':models.BolgPost.objects.all()
    }
    return render(request,'index.html',context)



def contact(request):
    return render(request,'contact.html')



def scrap(request):
    data = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        data = scrape_website(url=url)
    return render(request, 'scrap.html', {'data': data})