""" Module for generating products over $1000 """

from typing import List
from bangazonapi.models.product import Product
import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection

def cheap_products(request):
    """ Function to build an HTML report of products over $1000 """
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    id,
                    name,
                    price,
                    description
                FROM
                    bangazonapi_product
                WHERE
                    price < 1000
            """)

            dataset = db_cursor.fetchall()

            cheap_products = {}

            for row in dataset:
                product = Product()
                product.id = row["id"]
                product.name = row["name"]
                product.price = row["price"]
                product.description = row["description"]

                cheap_products[product.id] = product

    list_of_cheap_products = list(cheap_products.values())

    template = 'products/cheap_products.html'
    context = {
        'product_list': list_of_cheap_products
    }

    return render(request, template, context)

