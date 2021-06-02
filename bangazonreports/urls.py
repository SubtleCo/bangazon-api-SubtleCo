from django.urls import path
from .views import expensive_products, cheap_products

urlpatterns = [
    path('reports/expensiveproducts', expensive_products),
    path('reports/cheapproducts', cheap_products),
]
