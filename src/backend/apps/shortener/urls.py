from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('urls/', views.URLView.as_view(), name='urls'),
    path('url-redirect/<slug:slug>', views.URLRedirectView.as_view(), name='url-redirect')
]