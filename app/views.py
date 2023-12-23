from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q






# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    QLWO=Webpage.objects.all()
    #QLWO=Webpage.objects.all().order_by('-pk')
    QLWO=Webpage.objects.all().order_by('-name')
    #QLWO=Webpage.objects.filter(name__contains='r')
    #QLWO=Webpage.objects.filter(name__regex='\w+t$')
    #QLWO=Webpage.objects.all()
    #QLWO=Webpage.objects.filter(Q(topic_name='cricket'),Q(name__startswith='R'))
    
    #QLWO=Webpage.objects.filter(Q(topic_name='cricket'),Q(name__startswith='v'))
    #QLWO=Webpage.objects.all()
    #QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(url__endswith='i'))
    d={'webpage':QLWO}
    return render(request,'display_webpages.html',d)
def insert_topics(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'insert_topics.html',d)

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    To=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,email=e)[0]
    NWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('inserted Succesfully')
def insert_access(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'access':QLTO}
    return render(request,'display_access.html',d)

def display_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(id__lte=4)
    QLAO=AccessRecord.objects.filter(date='2023-12-07')
    d={'access':QLAO}
    return render(request,'display_access.html',d)

def update_webpage(request):
    #Webpage.objects.filter(topic_name='volley ball',defaults={'name':'virat'})
    Webpage.objects.filter(topic_name='Cricket').update(name='rohith')
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpages.html',d)

def delete_webpage(request):
    Webpage.objects.filter(name='virot').delete()
    #Webpage.objects.all.delete()
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpages.html',d)



