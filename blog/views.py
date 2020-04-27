from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date') 
    return render(request, 'blogs/all_blogs.html', {'blogs':blogs})

    # if we want to limits the no of blogs to get displayed on our website use [:number] i.e [:5] , if no limit is given all blogs will be fetched
    # and if we want blogs to be sorted by date and other stuffs use order_by('-date'), we passed date here
    #blogs = Blog.objects.order_by('-date') [:5]
    #blogs = Blog.objects.all()  , displays all blogs 
    #blog_count = Blog.objects.count  , can pass all blogs count


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)    # tries to grab particular id , else 404 will be displayed
    return render(request,'blogs/detail.html', {'blog':blog})


