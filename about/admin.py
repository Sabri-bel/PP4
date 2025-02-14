from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, TeamMember, ReservationRequest

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)


@admin.register(ReservationRequest)
class ReservationAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)


@admin.register(TeamMember)
class StaffAdmin(admin.ModelAdmin):
    """
    Lists details about the staff member fields for display in admin
    """
    list_staff = ('name', 'title', 'bio')
