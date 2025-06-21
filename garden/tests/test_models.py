from django.test import TestCase
from django.contrib.auth.models import User
from garden.models import Event, Participation

class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.event = Event.objects.create(
            organizer=self.user,
            title='Planting Day',
            description='Let’s plant trees!',
            location='Hyderabad',
            date='2025-06-28',
            time='10:00',
            capacity=20
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Planting Day')
        self.assertEqual(self.event.organizer.username, 'tester')
