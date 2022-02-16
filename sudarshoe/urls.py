from rest_framework import routers
from .views import *

urlpatterns = []

productRouter = routers.DefaultRouter()
transRouter = routers.DefaultRouter()

productRouter.register('product', ProductViewset, basename='product')
transRouter.register('transaction', TransactionViewset, basename='transaction')

urlpatterns += productRouter.urls
urlpatterns += transRouter.urls
