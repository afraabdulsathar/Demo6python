from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import profile


# Create your views here.
def cemo(request):
    obj=place.objects.all()
    ob=profile.objects.all()
    return render(request,"index.html",{'result':obj,'ans':ob})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res2=x-y
#     res3=x*y
#     res4=x//y
#     return render(request, "result.html",{'result':res,'result2':res2,'result3':res3,'result4':res4})
