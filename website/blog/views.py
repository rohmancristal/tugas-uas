from django.shortcuts import render
from .models import blog

def blogs(request):
    blogs = blog.objects.all()
    context ={
        'judul': 'ini adalah tampilan awal', 
        'blogs':blogs,
        
    }
    return render(request, 'blog/blog.html', context)

def blogsdetail(request, id):
    blogs = blog.objects.get(id =id)
    
    return render(request, 'blog/blogdetail.html', {'blogs':blogs})