from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, TeamMember, ReservationRequest

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(ReservationRequest)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)


@admin.register(TeamMember)
class StaffAdmin(admin.ModelAdmin):
    list_staff = ('name', 'title', 'bio')
