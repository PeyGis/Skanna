def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "title": product["title"],
        "url": product["url"],
        "image_url": product["image_url"],
        "description": product["description"],
        "brand": product["brand"],
        "price": product["price"],
        "stock_quantity": product["stock_quantity"],
        "category": product["category"],
        "sub_category": product["sub_category"],
        "rating": product["rating"],
        "num_verified_rating": product["num_verified_rating"],
    }

def products_serializer(products) -> list:
    return [product_serializer(product) for product in products] 
