from django.shortcuts import render
from .models import Article

# Create your views here.

def Home(request):
    articles = Article.objects.filter(status="p").order_by('-published')
    context = {
        "articles": articles
    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        "article": article
    }
    return render(request, 'blog/detail.html', context)