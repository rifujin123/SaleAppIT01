import json

def load_category():
    with open('data/category.json', encoding='utf-8') as file:
        return json.load(file)