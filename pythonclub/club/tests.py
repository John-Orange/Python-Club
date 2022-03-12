from datetime import datetime
from importlib import resources
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import ResourcesForm
from django.urls import reverse_lazy, reverse



# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingtitle='First')

    def test_meetingstring(self):
        self.assertEqual(str(self.type),'First')
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class ResourceTest(TestCase):
    def setUp(self):
        self.user = User(username='user1')

        self.resource1 = Resource(resourcename= 'Steam',
        resourcetype='Gaming application',
        resourceURL= 'https://store.steampowered.com/',
        enterdate=datetime.date(2022,2,9),
        userID=self.user, 
        resourcedescrip='Online Gaming Store' )

        self.resource2 = Resource(resourcename= 'Iphone 13',
        resourcetype='Smart Phone',
        resourceURL= 'https://www.apple.com/',
        enterdate=datetime.date(2022,2,9),
        userID=self.user,
        resourcedescrip='Phone' )

    def test_string(self):
        self.assertEqual(str(self.resource1), 'Steam')
        self.assertEqual(str(self.resource2), 'Iphone 13')

class NewResourcesForm(TestCase):
        #valid form data
    def test_ResourcesForm(self):
        self.data = {
            'resourcename' : 'Google',
            'resourcetype' : 'Search Engine',
            'resourceURL' : 'https://store.google.com/',
            'enterdate' : '2022-2-9',
            'userID' : 'User1',
            'resourcedescrip' : '',
             
            }
        form=ResourcesForm(self.data)
        self.assertTrue(form.is_valid)









# Homework 10

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):

        
        self.test_user=User.objects.create_user(username='User1', password='P@ssw0rd1')

        self.resource=Resource.objects.create(resourcename= 'Google', 
        resourcetype='Search Engine', 
        resourceURL='https://store.google.com/', 
        enterdate=datetime.date(2022,3,10), 
        userID=self.test_user,
        resourcedescrip= '' )

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newResource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newResource/')


    