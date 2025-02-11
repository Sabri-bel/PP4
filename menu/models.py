from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name="menu_posts"
                                )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-created_on"]


class Feedback(models.Model):
    post = models.ForeignKey(
                            Post,
                            on_delete=models.CASCADE,
                            related_name="feedbacks"
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


class TeamMember(models.Model):
    name =  models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    is_staff = models.BooleanField(default=False)