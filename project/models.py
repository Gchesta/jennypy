from django.db import models
from django.utils import timezone


class Presentation(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    first_presenter = models.ForeignKey('auth.User')
    #second_presenter = models.ForeignKey('auth.User')
    synopsis = models.TextField()
    sex =  models.CharField(max_length=200)

    def register(self, title, category, school, zone, first_presenter, second_presenter, synopsis):
        self.title = title
        self.category = category
        self.school = school
        self.zone = zone
        self.presenters = [first_presenter, second_presenter]
        self.synopsis = synopsis
        self.registration_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title