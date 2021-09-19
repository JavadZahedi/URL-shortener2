from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView


from rest_framework.permissions import AllowAny

from .serializers import URLSerializer
from .models import URL
from core.customs.viewsets import CustomModelViewSet

# Create your views here.

class URLViewSet(CustomModelViewSet):
    queryset = URL.objects.all()
    serializer_classes = {
        'default': URLSerializer
    }

    # def get_queryset(self):
    #     queryset = self.queryset
    #     sort_key = self.request.query_params.get('sort')
    #     print(sort_key)
    #     return queryset.order_by(sort_key)


class URLRedirectView(RedirectView):
    permanent = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address