from flask import Blueprint, render_template, session, redirect, url_for

from models.product import Product

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/cart")
def cart():

    cart_items = []

    total = 0

    cart = session.get("cart", {})

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            subtotal = product.price * quantity

            total += subtotal

            cart_items.append({

                "product": product,

                "quantity": quantity,

                "subtotal": subtotal

            })

    return render_template(

        "cart/cart.html",

        cart_items=cart_items,

        total=total

    )


@cart_bp.route("/cart/add/<int:product_id>")
def add_to_cart(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    cart[product_id] = cart.get(product_id, 0) + 1

    session["cart"] = cart

    session.modified = True

    return redirect(url_for("cart.cart"))


@cart_bp.route("/cart/remove/<int:product_id>")
def remove_from_cart(product_id):

    cart = session.get("cart", {})

    cart.pop(str(product_id), None)

    session["cart"] = cart

    session.modified = True

    return redirect(url_for("cart.cart"))


@cart_bp.route("/checkout")
def checkout():

    return render_template("cart/checkout.html")