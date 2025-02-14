from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Stores a single post entry related to :model:`auth.User`.

    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name="menu_posts"
                                )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    """
    Stores a single comment related to :model:`auth.User` and
    :model:`menu.Post`
    """
    post = models.ForeignKey(
                            Post,
                            on_delete=models.CASCADE,
                            related_name="comments"
                            )
    author = models.ForeignKey(
                            User,
                            on_delete=models.CASCADE,
                            related_name="commenter"
                            )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body} by {self.author}"

    class Meta:
        ordering = ["created_on"]
