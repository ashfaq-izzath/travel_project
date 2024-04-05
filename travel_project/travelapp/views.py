from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Mentors
# Create your views here.
# def demo(request):
#     value='...........'
#     return render(request,'basics.html',{'xyz':value})
#
# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return HttpResponse('hii this is my contact page')

def demo(request):
    obj1=Place.objects.all()
    obj2=Mentors.objects.all()
    return render(request,'1index.html',{'result1':obj1, 'result2':obj2})

# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     addres=x+y
#     subres=x-y
#     mulres=x*y
#     divres=x/y
#     return render(request,'result.html',{'addition':addres, 'subtraction':subres, 'multiplication':mulres, 'division':divres})