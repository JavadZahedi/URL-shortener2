from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'accounts'
urlpatterns = [
    # GET, POST, PUT, PATCH, DELETE
    path('', include(router.urls)),
    # GET
    path('set-csrf-cookie/', views.SetCSRFCookieView.as_view(),
         name='set-csrf-cookie'),
    # POST
    path('registration/', views.RegistrationView.as_view(), name='login'),
    # POST
    path('login/', views.LoginView.as_view(), name='login'),
    # POST
    path('logout/', views.LogoutView.as_view(), name='logout')
]