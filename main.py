import sys
import json 

from analyzer import (
    load_data,
    calculate_average_price,
    find_most_expensive_product,
    find_cheapest_product,
    calculate_total_stock,
    calculate_inventory_value,
    calculate_average_rating,
    count_products_by_category,
)


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        return

    file_path = sys.argv[1]
    try:
        products_data = load_data(file_path)
        if "products" not in products_data:
            print(f"Error: The file '{file_path}' does not contain a 'products' key.")
            return
    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return
    
    products = products_data["products"]

    average_price = calculate_average_price(products)
    most_expensive = find_most_expensive_product(products)
    cheapest = find_cheapest_product(products)
    total_stock = calculate_total_stock(products)
    inventory_value = calculate_inventory_value(products)
    average_rating = calculate_average_rating(products)
    category_counts = count_products_by_category(products)


    print("=" * 40)
    print("       E-COMMERCE PRODUCT ANALYZER")
    print("=" * 40)

    print("\nDATASET")
    print("-" * 7)
    print(f"Products analyzed: {len(products)}")

    print("\nPRICING")
    print("-" * 7)
    print(f"Average price:       ${average_price:.2f}")
    print(
        f"Most expensive:      {most_expensive['title']} "
        f"(${most_expensive['price']:.2f})"
    )
    print(
        f"Cheapest:            {cheapest['title']} "
        f"(${cheapest['price']:.2f})"
    )

    print("\nINVENTORY")
    print("-" * 9)
    print(f"Total stock:         {total_stock:,} units")
    print(f"Inventory value:     ${inventory_value:,.2f}")

    print("\nRATINGS")
    print("-" * 7)
    print(f"Average rating:      {average_rating:.2f}")

    print("\nCATEGORIES")
    print("-" * 10)

    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()