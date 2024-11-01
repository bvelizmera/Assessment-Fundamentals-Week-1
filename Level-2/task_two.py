"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

def add_to_basket(item: dict) -> list:
    """This function will add the items to the basket"""
    basket.append(item)
    return basket
def generate_receipt(basket: list) -> str:
    """It will generate a receipt to be printed later on"""
    receipt = ""
    single_items = []

    for item in basket:
        if item not in single_items:
            single_items.append(item)

    for individual_item in single_items:

        receipt += (f"{individual_item["name"]} x {basket.count(individual_item)} - £{individual_item["price"]*basket.count(individual_item):.2f}\n")
    total_price = 0
    if len(basket) == 0:
        return "Basket is empty"
    for item in basket:
        price = item["price"]
        total_price += price
    return  receipt + f"Total: £{total_price:.2f}"# return the receipt string

def convert_price_to_str(price:float) -> str:
    """This function converts the prices to a string or to free if value is 0"""
    if price == 0:
        return "Free"

    return f"£{price:.2f}"

if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))

# print(items_counter(basket))
