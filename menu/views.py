from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Feedback, TeamMember

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "menu/index.html"
    paginate_by = 10


def create_recipe(request):
    if not request.user.is_staff:
        return redirect('login')
    

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "menu/post_detail.html", {"post": post},)