from django.shortcuts import render, redirect
from .models import Post
from .forms.add_publication_form import AddPublicationForm


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-create_date', '-id').all()
    context = {'title': 'insta django_app', 'posts': posts}
    return render(request, "main_page.html", context)


def add_publication_page(request):
    if request.method == 'POST':
        form = AddPublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddPublicationForm()
    context = {'title': 'add_publication', 'add_publication_form': form}
    return render(request, "add_publication_page.html", context)
