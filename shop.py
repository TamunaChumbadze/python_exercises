inventory = [
    {
        "name": "Vintage T-shirt",
        "price": 29.99,
        "stock": 41,
    },
    {
        "name": "Coffe Mug",
        "price": 12.50,
        "stock": 100,
    },
    {
        "name": "Laptop Sticker Pack",
        "price": 5.00,
        "stock": 250,
    }

]

cart = {}

def display_products(inventory):
    for index, item in enumerate(inventory):
        print(
            f"{index + 1}. Name: {item['name']} - Price: ${item['price']} - Stock: {item['stock']}"
        )
   
def add_to_cart(inventory, cart):
    # ask product id
    product_id = int(input("Product number: "))
    quantity = int(input("Quantity: "))
    # validation
    if product_id > 0 and product_id <= len(inventory):
       
        if quantity <= inventory[product_id - 1]["stock"]:
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
    else:
        print("Invalid product number.")
# checking available stock

    
   

display_products(inventory)