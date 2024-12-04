from django.shortcuts import render

# Create your views here.

def jinja_condition(request):
    d={'name':'Jhon','age':26}
    return render(request,'jinja_condition.html',context=d)