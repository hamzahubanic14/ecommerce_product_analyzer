import requests
import json


response = requests.get("https://dummyjson.com/products")


data = response.json()

with open("products.json", "w") as file:
    json.dump(data, file, indent=4)


def load_data(file_path: str):
    with open(file_path, "r") as file:  
        return json.load(file)

products_data = load_data("products.json")

products = products_data["products"]



def calculate_average_price(products: list) -> float:
    total_price = 0

    for product in products:
        total_price += product["price"]

    average_price = total_price / len(products)

    return average_price
    

def find_most_expensive_product(products: list) -> dict:
    most_expensive_product = products[0]

    for product in products:
        if product["price"] > most_expensive_product["price"]:
            most_expensive_product = product

    return most_expensive_product


def find_cheapest_product(products: list) -> dict:
    cheapest_product = products[0]

    for product in products:
        if product["price"] < cheapest_product["price"]:
            cheapest_product = product

    return cheapest_product



def calculate_total_stock(products: list) -> int:
    total_stock = 0

    for product in products:
        total_stock += product["stock"]

    return total_stock


def calculate_inventory_value(products: list) -> float:
    total_value = 0

    for product in products:
        total_value += product["price"] * product["stock"]

    return total_value



def calculate_average_rating(products: list) -> float:
    total_rating = 0

    for product in products:
        total_rating += product["rating"]

    average_rating = total_rating / len(products)

    return average_rating




def count_products_by_category(products: list) -> dict:
    category_count = {}

    for product in products:
        category = product["category"]
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

    return category_count



