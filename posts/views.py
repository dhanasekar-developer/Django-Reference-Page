from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from . forms import PostForm
import logging
from django.contrib.auth.decorators import login_required

# Create your views here.
logger = logging.getLogger("TESTING")
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url='/user/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect("posts:list")
    else:
            form = PostForm()
    # logger.debug(f'form value is : {form}')
    return render(request, 'posts/post_new.html', {'form': form})