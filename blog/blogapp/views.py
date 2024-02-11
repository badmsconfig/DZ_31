from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ContactForm

# Create your views here.
def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def create_post(request):
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
    return render(request, 'blogapp/create.html')

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})