from django.shortcuts import render
from django.contrib import messages
from .models import About, TeamMember
from .forms import ReservationForm

# Create your views here.


def about_me(request):
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request, 
                                 messages.SUCCESS,
                                 "reservation request submitted! we will reply in 2 working days")
    about = About.objects.all().order_by('updated_on').first()
    reservation_form = ReservationForm()
    return render(request, "about/about.html", {
                                                "about": about,
                                                "reservation_form": reservation_form
                                                },)


def staff(request):
    staff = TeamMember.objects.all()
    template = "about.html"
    context = {"about": "TeamMember",
               "staff": staff}
    
    return render(request, template, context)