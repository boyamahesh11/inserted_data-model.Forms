from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tfo=TopicForm()
    d={'tfo':tfo}
    if request.method=='POST':
        tfdo=TopicForm(request.POST)
        if tfdo.is_valid():
            tfdo.save()
            return HttpResponse('topic inserted sucessfully!!')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    wfo=WebpageForm()
    d={'wfo':wfo}
    if request.method=='POST':
        wd=WebpageForm(request.POST)
        if wd.is_valid():
            wd.save()
        return HttpResponse('webpage is inserted sucessfully!!')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    afo=AccessForm()
    d={'afo':afo}
    if request.method=='POST':
        afod=AccessForm(request.POST)
        if afod.is_valid():
            afod.save()
        return HttpResponse('acess data inserted sucessfully')
    return render(request,'insert_access.html',d)
    