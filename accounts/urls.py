from django import views
from django.urls import path
from . views import *
from rest_framework import routers

account_router = routers.DefaultRouter()
account_router.register('', AccountViewsets, basename='account')

urlpatterns = [    
    path('signup/', SignupViewsets.as_view()),
    path('login/', LoginViewsets.as_view()),
    path('logout/', LogoutViewsets.as_view())
]

urlpatterns += account_router.urls