from django.shortcuts import render
# from django.http import HttpResponse
from .models import dictionary



def index(request):
    word = request.GET.get('q', '')
    if word and word !=  '':
        result = dictionary.objects.filter(chinese__contains=word).all()[:3]
        if result == '':
            result = dictionary.objects.filter(english__contains=word).all()[:3]
    else:
        result = None
    return render(request, 'index.html', {'q':word, 'result':result})


# def hello(request):
#     return HttpResponse("<h1>hello</h1>")
