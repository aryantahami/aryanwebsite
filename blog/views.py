from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def listing_page(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/listing_page.html', {'posts_list': posts_list})


def detail_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail_page.html', {'post': post})




    # print('ID IN URL:', pk)
    # return HttpResponse(f'Id: {pk}')


    # post = Post.objects.get(pk=pk)
    # return render(request, 'blog/detail_page.html', {'post': post})


    # return HttpResponse('hellooooooooooooooo')

    # posts_list = Post.objects.all()
    # return render(request, 'blog/detail_page.html', {'posts_list': posts_list})


