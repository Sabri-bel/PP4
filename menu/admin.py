from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Feedback


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    provide some editor function to the admin panel
    """
    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content")


# Register your models here.


admin.site.register(Feedback)
