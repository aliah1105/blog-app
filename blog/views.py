from django.shortcuts import render

# Create your views here.

def Home(request):
    context = {
        "articles": [
            {
                "title": "first articl",
                "description": "this is a first description"
            },
            {
                "title": "second articl",
                "description": "this is a second description"
            },
            {
                "title": "third articl",
                "description": "this is a third description"
            }
        ]

    }
    return render(request, 'blog/home.html', context)
