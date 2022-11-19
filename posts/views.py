from django.shortcuts import render
import datetime
from .models import *
def hello(request):
    return render(request, 'hello.html')
def goodby (request):
    return render(request, 'goodby.html')
def now_date (request):
    a = datetime.datetime.now()
    return render(request, 'now_date.html',{'a':a})



def hashtags(request):
    if request.method == "GET":
        data = {'hashtags': Hashtag.objects.all()}
        return render(request, 'hashtags.html', context=data)


def posts(request):
    data = {'posts': Post.objects.all()}
    return render(request, 'posts.html', context=data)
