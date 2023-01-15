from django.shortcuts import render

from .models import Post


def listing_page(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/listing-page.html', {'posts_list': posts_list})


def detail_page(request):
    return render(request, 'blog/detail-page.html')
