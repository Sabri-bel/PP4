from django.shortcuts import render
from django.contrib import messages
from .models import About, TeamMember
from .forms import ReservationForm

# Create your views here.


def about(request):
    """
    render the most recent information on the website restaurant information
    and restaurant staff, and allow reservation request
    Displays an individual instance of :model:`about.About`
    ***context***
    ``about``
        the most recent instance of instance of :model:`about.About`
    ``team member``
        all the records related to the :model:`about.TeamMember`
    ``reservation form``
        an instance of :form:`about.ReservationForm`
    :template: about/about.html

    """
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "reservation request"
                                 "submitted! we will reply"
                                 "in 2 working days")
    about = About.objects.all().order_by('updated_on').first()
    team_members = TeamMember.objects.all()

    reservation_form = ReservationForm()
    return render(request,
                  "about/about.html",
                  {
                    "about": about,
                    "team_members": team_members,
                    "reservation_form": reservation_form
                    },)
