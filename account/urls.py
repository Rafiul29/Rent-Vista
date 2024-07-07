from django.urls import path
from .views import UserRegistrationView,activate,UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('active/<uid64>/<token>/',activate,name='active')
]
