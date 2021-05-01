from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog_en,Keyword
from django.db.models import Count
from datetime import datetime

# Create your views here.
def index(request):
    # Counts how many times a keyword was referenced, Returns just the keywords referenced at least once
    keys = list(Blog_en.objects.values("keywords__keyword").annotate(Count('keywords__keyword')))
    context = {
        'keys': keys
    }
    # TODO Read the documentation to create the cloud word with the most used keywords
    return render(request,'blog/index.html',context)

def open_post(request, slug):
     #('blog/open_post.html',
     context = {
         'post': get_object_or_404(Blog_en.objects.values('title', 'body', 'description'), url=slug),
         'keywords': list(Blog_en.objects.values('keywords__keyword').filter(url=slug))
     }
     print(context)
     return render(request, 'blog/open_post.html', context)

def open_keyword(request, slug):
    post = list(Blog_en.objects.values('title', 'img', 'description','url').filter(keywords__keyword=slug))
    print(post)
    context = {
        'post': post,
        'slug': slug
    }

    return render(request,'blog/open_category.html',context)

