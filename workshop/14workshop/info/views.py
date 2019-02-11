from django.shortcuts import render
from .models import Post

# Create your views here.
def info(request) :
    posts = Post.objects.all()
    return render(request,"info.html",{"posts":posts})
    
def student(request,title):
    post = Post.objects.get(title=title)
    title = post.title
    content = post.content
    return render(request,"student.html",{"title":title,"content":content})