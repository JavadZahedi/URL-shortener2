from rest_framework import serializers

from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('label', 'address', 'slug', 'visits')
        read_only_fields = ('visits', 'slug')