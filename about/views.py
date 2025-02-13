from django.shortcuts import render
from django.contrib import messages
from .models import About, TeamMember
from .forms import ReservationForm

# Create your views here.


def about(request):
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request, 
                                 messages.SUCCESS,
                                 "reservation request submitted! we will reply in 2 working days")
    about = About.objects.all().order_by('updated_on').first()
    team_members = TeamMember.objects.all()

    reservation_form = ReservationForm()
    return render(request, "about/about.html", {
                                                "about": about,
                                                "team_members": team_members,
                                                "reservation_form": reservation_form
                                                },)
