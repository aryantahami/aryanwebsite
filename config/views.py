from django.http import HttpResponse


def main_page(request):
    return HttpResponse("you are in main page")
