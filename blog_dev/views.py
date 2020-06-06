from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog_en
# Create your views here.
def index(request):
    return render(request, 'index.html')

def open_post(request, slug):
     #('blog/open_post.html',
     context = {
         'post': get_object_or_404(Blog_en.objects.values('title', 'body'), url=slug),
         'keywords': list(Blog_en.objects.values('keywords__keyword').filter(url=slug))
     }
     print(context)
     return render(request, 'blog/open_post.html', context)
