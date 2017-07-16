from django.shortcuts import render, get_object_or_404
from django.utils import timezone as tz
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(date_published__lte=tz.now()).order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
