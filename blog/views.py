import re

from django.shortcuts import render, get_object_or_404

# Create your views here.
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from blog.models import Post


def index(request):
    # return HttpResponse("欢迎！")
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
    # return render(request, 'blog/index.html')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)

    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})
