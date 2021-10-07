from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .serializers import URLSerializer
from .models import URL
from core.customs.viewsets import CustomModelViewSet

# Create your views here.

class URLViewSet(CustomModelViewSet):
    queryset = URL.objects.all()
    serializer_classes = {
        'default': URLSerializer
    }
    permission_classes = {
        'default': (IsAuthenticatedOrReadOnly,)
        # 'default': (AllowAny,)
    }


class URLRedirectView(RedirectView):
    permanent = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address