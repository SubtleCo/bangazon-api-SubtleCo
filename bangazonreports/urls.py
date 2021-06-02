from django.urls import path
from .views import expensive_products, completed_orders, incomplete_orders

urlpatterns = [
    path('reports/expensiveproducts', expensive_products),
    path('reports/orders/completed', completed_orders),
    path('reports/orders/incomplete', incomplete_orders),
]
