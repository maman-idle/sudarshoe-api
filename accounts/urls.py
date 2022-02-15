from django import views
from django.urls import path
from . views import *

urlpatterns = [
    path('', AccountViewsets.as_view()),
    path('signup/', SignupViewsets.as_view()),
    path('logout/', LogoutViewsets.as_view())
]