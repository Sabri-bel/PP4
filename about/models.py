from django.db import models

# Create your models here.


class About(models.Model):
    """
    Stores a single about me record.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """
    Store a single team member information
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} is the {self.title}"


class ReservationRequest(models.Model):
    """
    Stores a single reservation request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    res_date = models.DateTimeField(auto_now=True)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation request from {self.name}"
