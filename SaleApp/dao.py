import json


def load_category():
    with open('data/category.json', encoding='utf-8') as file:
        return json.load(file)


def load_products(q=None, cate_id=None):
    with open('data/product.json', encoding='utf-8') as product:
        products = json.load(product)

        if q:
            products = [p for p in products if p["name"].find(q) >= 0]

        if cate_id:
            cate_id = [p for p in products if p["cate_id"] == int(cate_id)]

        return products
