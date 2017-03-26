from django.shortcuts import render

def presentation_list(request):
    return render(request, 'project/presentation_list.html', {})

# Create your views here.
