from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def Resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'club/Resources.html',{'resources_list': resources_list})

def Meetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/Meetings.html',{'meetings_list': meetings_list})

def MeetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/MeetingDetail.html',{'meeting': meeting})