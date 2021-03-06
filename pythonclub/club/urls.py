from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('Resources/', views.Resources, name='Resources'),
    path('ResourceDetail/<int:id>', views.ResourceDetail, name='Resource detail'),
    path('Meetings/', views.Meetings, name='Meetings'),
    path('MeetingDetail/<int:id>', views.MeetingDetail, name='Meeting detail'),
    path('newResource/', views.newResource, name='newResource'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]
