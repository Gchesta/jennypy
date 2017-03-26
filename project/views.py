from django.shortcuts import render
from .models import Presentation
from django.utils import timezone

def presentation_list(request):
    presentations = Presentation.objects.all()
    return render(request, 'project/presentation_list.html', {'presentations':presentations})

# Create your views here.
