from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Event, Participation, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['interests', 'skills']  # ✅ changed from 'bio' to 'interests'

class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Participation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
