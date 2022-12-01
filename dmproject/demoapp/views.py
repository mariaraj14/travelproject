from django.shortcuts import render
from django.http import HttpResponse
from.models import place
from.models import people
# Create your views here.
def demo(request):
    obj=place.objects.all()
    ob=people.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})
# def add(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     a=x+y
#     s=x-y
#     m=x*y
#     d=x/y

    #return render(request,"about.html",{'addres':a,'subres':s,'mulres':m,'divres':d})
#def contact(request):
 #   return render(request,"contact.html")
#def detail(request):
 #   return HttpResponse("this is detail page")