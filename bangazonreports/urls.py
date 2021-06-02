from django.urls import path
from .views import expensive_products, completed_orders

urlpatterns = [
    path('reports/expensiveproducts', expensive_products),
    path('reports/orders/completed', completed_orders),
]
