from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostList(ListView):
    queryset = Post.objects.order_by('-updated_on')
    context_object_name = 'posts'
    paginate_by     = 1
    template_name = 'blog/home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'