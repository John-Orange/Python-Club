from datetime import datetime
from importlib import resources
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime



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
        self.resource1 = Resource(resourcename= 'Steam', resourcetype='Gaming application', resourceURL= 'https://store.steampowered.com/', enterdate=datetime.date(2022,2,9), userID=self.user,  resourcedescrip='Online Gaming Store' )
        self.resource2 = Resource(resourcename= 'Iphone 13', resourcetype='Smart Phone', resourceURL= 'https://www.apple.com/', enterdate=datetime.date(2022,2,9), userID=self.user,  resourcedescrip='Phone' )

    def test_string(self):
        self.assertEqual(str(self.resource1), 'Steam')
        self.assertEqual(str(self.resource2), 'Iphone 13')

    