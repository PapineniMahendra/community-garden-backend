from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from garden.models import Event

class EventTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='eventuser', password='pass')

    def test_event_listing(self):
        Event.objects.create(
            organizer=self.user,
            title='Gardening',
            description='Event Desc',
            location='Location',
            date='2025-07-15',
            time='09:00',
            capacity=10
        )
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)
