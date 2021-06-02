""" Module for generating completed orders """

from bangazonapi.models.order import Order
import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection

def incomplete_orders(request):
    """ Function to build an HTML report of completed orders """
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    o.id id,
                    u.first_name ||' '|| u.last_name Name,
                    COALESCE(SUM(p.price), '0') Total
                FROM
                    bangazonapi_order o
                JOIN
                    bangazonapi_orderproduct op ON o.id = op.order_id
                JOIN
                    bangazonapi_product p ON p.id = op.product_id
                JOIN
                    bangazonapi_customer c ON c.id = o.customer_id
                JOIN
                    auth_user u ON c.id = u.id
                WHERE
                    o.payment_type_id IS NULL
                GROUP BY o.id;
            """)

            dataset = db_cursor.fetchall()

            orders= {}

            for row in dataset:
                order = Order()
                order.id = row["id"]
                order.name = row["Name"]
                order.total = row["Total"]

                orders[order.id] = order

    list_of_orders = list(orders.values())

    template = 'orders/incomplete_orders.html'
    context = {
        'orders_list': list_of_orders
    }

    return render(request, template, context)

