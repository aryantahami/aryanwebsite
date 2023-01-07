from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def myhttp(request):
    return HttpResponse("hello aryan")


def aryan_html(request):
    return render(request, 'pages/page-html.html')
    # # update down syntax
    # response_data = render_to_string('pages/page-html.html')
    # return HttpResponse(response_data)
