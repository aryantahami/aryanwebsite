from django.shortcuts import render


def templatemo(request):
    return render(request, 'templatemo/index.html')
