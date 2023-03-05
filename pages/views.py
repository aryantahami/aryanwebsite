from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Article


def myhttp(request):
    return HttpResponse("hello aryan")


def aryan_html(request):
    article = Article.objects.all()
    context = {
        'my_article': article,
    }
    return render(request, 'pages/page-html.html', context)
    # # update down syntax
    # response_data = render_to_string('pages/page-html.html')
    # return HttpResponse(response_data)


def cats(request):
    return render(request, 'pages/cats.html')


def dogs(request):
    return render(request, 'pages/dogs.html')


def birds(request):
    return render(request, 'pages/birds.html')


def rodents(request):
    return render(request, 'pages/rodents.html')


def reptiles(request):
    return render(request, 'pages/reptiles.html')
