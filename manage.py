from django.shortcuts import render
def home(request):
    print('request', request)
    name ="john"
    return render(request,'new.html',{"name":name
    })