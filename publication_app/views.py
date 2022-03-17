from django.shortcuts import render
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-create_date', '-id').all()
    context = {'title': 'insta django_app', 'posts': posts}
    return render(request, "main_page.html", context)
