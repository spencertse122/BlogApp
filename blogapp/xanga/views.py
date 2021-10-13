from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse 
from .models import Post


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Xanga index.")

def some_view(request):
    return render(request, 'xanga.html', {})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




