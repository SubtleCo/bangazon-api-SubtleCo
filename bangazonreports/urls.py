from django.urls import path
from .views import expensive_products, completed_orders, incomplete_orders, favorited_sellers, cheap_products

urlpatterns = [
    path('reports/expensiveproducts', expensive_products),
    path('reports/orders/completed', completed_orders),
    path('reports/orders/incomplete', incomplete_orders),
    path('reports/customers/favorites', favorited_sellers),
    path('reports/cheapproducts', cheap_products),
]
