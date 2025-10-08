from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts_list = Post.objects.all()
    context = {
        'posts':posts_list
    }
    return render(request,context)


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        'post':post
    }
    return render(request,context)