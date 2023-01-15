from django.shortcuts import render


def main_page(request):
    return render(request, 'templatemo/index.html')


def about(request):
    return render(request, 'templatemo/about.html')


def contact(request):
    return render(request, 'templatemo/contact.html')

