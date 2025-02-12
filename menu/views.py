from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'your comment is awaiting approval')

    comment_form = CommentForm()

    return render(request,
                   "menu/post_detail.html",
                  {
                    "post": post,
                    "comments": comments,
                    "comment_count": comment_count,
                    "comment_form": comment_form,
                  },
                 )