from django.shortcuts import render
from .models import Post


def tag_page(request, hashtag):
    posts = Post.objects.filter(hashtag__title=hashtag).order_by('-create_date').all()
    context = {'title': f'tag_{hashtag}_page', 'posts': posts, 'hashtag': hashtag}
    return render(request, "hashtag_page.html", context)
