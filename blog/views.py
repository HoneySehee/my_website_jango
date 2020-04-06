from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):                          #포스트 리스트로 보여줌
    model = Post

    def get_queryset(self):                         #포스트 역순으로
        return Post.objects.order_by('-created')

# def index(request):
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#    )