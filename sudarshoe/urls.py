from rest_framework import routers
from .views import *
from django.urls import path

urlpatterns = [
    path('shoes/', ShoesList, name='shoes-list'),
    path('transaction-list/', TransListView.as_view())
]

productRouter = routers.DefaultRouter()
transRouter = routers.DefaultRouter()

productRouter.register('product', ProductViewset, basename='product')
transRouter.register('transaction', TransactionViewset, basename='transaction')

urlpatterns += productRouter.urls
urlpatterns += transRouter.urls

