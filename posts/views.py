from django.shortcuts import render
import datetime

def hello(request):
    return render(request, 'hello.html')
def goodby (request):
    return render(request, 'goodby.html')
def now_date (request):
    a = datetime.datetime.now()
    return render(request, 'now_date.html',{'a':a})
