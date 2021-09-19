from rest_framework import serializers

from .models import URL

class URLSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = (
            'label', 'address', 'slug', 'visits', 'created', 'last_visit'
        )
        read_only_fields = ('slug', 'visits', 'created', 'last_visit')