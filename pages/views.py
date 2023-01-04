from django.shortcuts import render
from django.http import HttpResponse


def myhttp(request):
    return HttpResponse("hello aryan")
