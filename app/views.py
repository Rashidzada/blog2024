from django.shortcuts import render
from .import models
# Create your views here.
def index(request):
    context = {
        'blogs':models.BolgPost.objects.all()
    }
    return render(request,'index.html',context)



def contact(request):
    return render(request,'contact.html')