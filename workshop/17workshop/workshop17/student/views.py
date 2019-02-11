from django.shortcuts import render

# Create your views here.
def student(request) :
    return render(request,"student.html")
    
def person(request,name) :
    return render(request,"person.html",{"name":name})