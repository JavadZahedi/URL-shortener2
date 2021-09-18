from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    # GET, POST
    path('urls/', views.URLView.as_view(), name='urls'),
    # GET
    path('url-redirect/<slug:slug>',
          views.URLRedirectView.as_view(),
          name='url-redirect'),
]