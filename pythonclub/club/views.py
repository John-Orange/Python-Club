from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def Resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'club/Resources.html',{'resources_list': resources_list})