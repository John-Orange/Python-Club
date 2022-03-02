from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourcesForm
from django.contrib.auth.decorators import login_required

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


@login_required
def newResource(request):
    form=ResourcesForm

    if request.method=='POST':
        form=ResourcesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourcesForm()
    else:
        form=ResourcesForm()
    return render(request, 'club/newResource.html', {'form':form})

@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newMeeting.html', {'form':form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')


