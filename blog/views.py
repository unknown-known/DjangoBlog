from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def index(request):
    # return HttpResponse("欢迎！")
    post_list = Post.objects.all().order_by('-create_time')
    for post in post_list:
        print(post.title)
    return render(request, 'blog/index.html', context={'post_list': post_list})
    # return render(request, 'blog/index.html')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})