from django.shortcuts import render
from django.views import generic
from .models import Post, Feedback, TeamMember

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "menu/index.html"
    paginate_by = 10

