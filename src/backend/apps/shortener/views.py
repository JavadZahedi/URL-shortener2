from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import URLSerializer
from .models import URL
from .paginations import CustomPagination
from apps.utils.slug_generation import generate_slug

# Create your views here.

class URLView(generics.ListCreateAPIView):
    serializer_class = URLSerializer

    def get_queryset(self):
        queryset = URL.objects.all()
        sort_keys = self.request.data.get('sort', [])
        for key in sort_keys:
            queryset = queryset.order_by(key)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(slug=generate_slug())


class URLRedirectView(RedirectView):
    permanent = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address