""" Module for generating customers with favorited sellers """

from bangazonapi.models.customer import Customer
from bangazonapi.models.order import Order
import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection


def favorited_sellers(request):
    """ Function to build an HTML report of completed orders """
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    c.id id,
                    u.first_name ||' '|| u.last_name name,
                    seller.first_name || ' ' || seller.last_name seller_name
                FROM
                    bangazonapi_customer c
                JOIN
                    auth_user u ON c.id = u.id
                JOIN
                    bangazonapi_favorite f ON f.customer_id = c.id
                JOIN
                    auth_user seller ON seller.id = f.seller_id
            """)

            dataset = db_cursor.fetchall()

            customers= {}

            for row in dataset:
                customer = Customer
                customer.name = row["name"]
                customer.favorite = row["seller_name"]

                uid = row["id"]

                if uid in customers:
                    customers[uid]['favorites'].append(customer.favorite)
                else:
                    customers[uid] = {}
                    customers[uid]["id"] = uid
                    customers[uid]["name"] = customer.name
                    customers[uid]["favorites"] = [customer.favorite]

            

    list_of_customers = list(customers.values())

    template = 'customers/favorited_sellers.html'
    context = {
        'customers': list_of_customers
    }

    return render(request, template, context)
