from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.


def home(request):
    # Get search query from GET parameters
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Filter news posts based on search query
        # Search in title, description, and author fields
        news_posts = NewsPost.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    else:
        # If no search query, show all posts
        news_posts = NewsPost.objects.all()
    
    context = {
        'news_posts': news_posts,
        'search_query': search_query
    }
    return render(request, "newsposts.html", context)


@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return redirect('home')
    else:
        form = NewsPostForm()
    
    context = {
        'form': form,
        'is_edit': False
    }
    return render(request, "write.html", context)


@login_required
def edit_news(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    
    # Check if the user is the author of the post
    if post.author != request.user.username:
        return redirect('home')  # Redirect if not the author
    
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES, instance=post)
        print(f"Form is valid: {form.is_valid()}")
        if form.is_valid():
            print(f"Saving post with title: {form.instance.title}")
            print(f"Author: {form.instance.author}")
            form.save()
            return redirect('home')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = NewsPostForm(instance=post)
    
    context = {
        'form': form,
        'is_edit': True,
        'post': post
    }
    return render(request, "write.html", context)


def read_page(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    context = {
        'post': post
    }
    return render(request, "read.html", context)


@login_required
def delete_news(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    
    # Check if the user is the author of the post
    if post.author != request.user.username:
        return redirect('home')  # Redirect if not the author
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {
        'post': post
    }
    return render(request, "delete_confirm.html", context)
