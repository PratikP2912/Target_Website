from flask import Blueprint, render_template, abort, request

from models.product import Product

products_bp = Blueprint("products", __name__)


@products_bp.route("/products")
def products_page():

    search = request.args.get("search", "")

    if search:

        products = Product.query.filter(
            Product.name.ilike(f"%{search}%")
        ).all()

    else:

        products = Product.query.all()

    return render_template(
        "products/products.html",
        products=products
    )


@products_bp.route("/product/<int:product_id>")
def product_details(product_id):

    product = Product.query.get(product_id)

    if not product:

        abort(404)

    return render_template(
        "products/product_details.html",
        product=product
    )