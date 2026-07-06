from app import app
from models import db
from models.product import Product


products = [

    Product(
        name="NVIDIA RTX 5070",
        brand="NVIDIA",
        category="GPU",
        price=64999,
        image="gpu1.jpg",
        description="High-performance graphics card for 1440p and 4K gaming.",
        rating=4.9,
        stock=10
    ),

    Product(
        name="AMD RX 9070 XT",
        brand="AMD",
        category="GPU",
        price=59999,
        image="gpu2.jpg",
        description="Excellent gaming performance with 16GB VRAM.",
        rating=4.8,
        stock=8
    ),

    Product(
        name="Ryzen 7 9800X3D",
        brand="AMD",
        category="CPU",
        price=48999,
        image="cpu1.jpg",
        description="Top-tier gaming processor.",
        rating=5,
        stock=12
    ),

    Product(
        name="Intel i7-14700K",
        brand="Intel",
        category="CPU",
        price=40999,
        image="cpu2.jpg",
        description="Powerful processor for gaming and productivity.",
        rating=4.7,
        stock=15
    ),

    Product(
        name="MSI MAG 27Q",
        brand="MSI",
        category="Monitor",
        price=25999,
        image="monitor1.jpg",
        description="27-inch QHD Gaming Monitor.",
        rating=4.8,
        stock=20
    ),

    Product(
        name="ASUS ROG Swift",
        brand="ASUS",
        category="Monitor",
        price=39999,
        image="monitor2.jpg",
        description="High refresh rate esports monitor.",
        rating=4.9,
        stock=6
    ),

    Product(
        name="Logitech G Pro X Keyboard",
        brand="Logitech",
        category="Keyboard",
        price=12999,
        image="keyboard1.jpg",
        description="Mechanical RGB gaming keyboard.",
        rating=4.6,
        stock=25
    ),

    Product(
        name="Logitech G502 X",
        brand="Logitech",
        category="Mouse",
        price=6499,
        image="mouse1.jpg",
        description="Precision gaming mouse.",
        rating=4.8,
        stock=30
    ),

    Product(
        name="HyperX Cloud III",
        brand="HyperX",
        category="Headset",
        price=8999,
        image="headset1.jpg",
        description="Comfortable gaming headset.",
        rating=4.7,
        stock=18
    ),

    Product(
        name="Samsung 990 PRO 2TB",
        brand="Samsung",
        category="SSD",
        price=19999,
        image="ssd1.jpg",
        description="PCIe Gen4 NVMe SSD.",
        rating=4.9,
        stock=14
    )

]


with app.app_context():

    if Product.query.count() == 0:

        db.session.add_all(products)

        db.session.commit()

        print("Products inserted.")

    else:

        print("Products already exist.")