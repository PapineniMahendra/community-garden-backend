import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['date', 'location']
