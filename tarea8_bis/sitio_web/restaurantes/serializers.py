from rest_framework_mongoengine import serializers
from rest_framework_mongoengine import viewsets

from .models import restaurants

class restaurantsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = restaurants
        fields = ('name', 'cuisine', 'borough', 'address', 'photo')

class restaurantsViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    serializer_class = restaurantsSerializer

    def get_queryset(self):
        return restaurants.objects.all()
