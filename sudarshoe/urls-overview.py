from django.urls import path
from .views import ApiOverview

urlpatterns = [path('', ApiOverview, name="api-overview"),]