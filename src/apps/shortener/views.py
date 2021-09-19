from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import URLSerializer
from .models import URL

# Create your views here.

class URLViewSet(generics.ListCreateAPIView):
    serializer_class = URLSerializer

    def get_queryset(self):
        queryset = URL.objects.all()
        sort_keys = self.request.data.get('sort', [])
        for key in sort_keys:
            queryset = queryset.order_by(key)
        return queryset


class URLRedirectView(RedirectView):
    permanent = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address