from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from garden.models import Event

class EventViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.client.login(username='user1', password='pass')

    def test_create_event(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'location': 'Kurnool',
            'date': '2025-07-01',
            'time': '15:00',
            'capacity': 30
        }
        response = self.client.post('/api/events/', data)
        self.assertEqual(response.status_code, 201)
