from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'urls', views.URLViewSet)

app_name = 'shortener'
urlpatterns = [
    # GET, POST, PUT, PATCH, DELETE
    path('', include(router.urls)),
    # GET
    path('url-redirect/<slug:slug>',
          views.URLRedirectView.as_view(),
          name='url-redirect'),
]