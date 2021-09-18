from django.urls import path
from . import views

app_name = 'public'
urlpatterns = [
    # GET
    path('', views.IndexView.as_view(), name='home'),
]