from django.shortcuts import render
from .models import blogContent
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    blogs = blogContent.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

def blog_details(request, blog_id):
    blogs = get_object_or_404(blogContent, pk=blog_id)
    return render(request , 'blog/blog_details.html',{'blogs': blogs} ) 