import random
import string
import os
import csv
category_items = {
    "Cookware": ["Frying Pan", "Saucepan", "Dutch Oven", "Wok"],
    "Bakeware": ["Cake Pan", "Loaf Pan", "Muffin Tin"],
    "Knives": ["Chef's Knife", "Paring Knife", "Bread Knife"],
    "Dishes": ["Plates", "Bowls", "Glasses", "Mugs"],
    "Appliances": ["Blender", "Toaster", "Microwave"],
    "Storage": ["Food Containers", "Spice Rack", "Dish Rack"],
    "Cleaning": ["Dish Soap", "Sponges", "Microfiber Cloths"],
    "Textile": ["Kitchen Towels", "Oven Mitts", "Apron"],
}

item_prices = {
    "Frying Pan": 25.99,
    "Saucepan": 19.99,
    "Dutch Oven": 79.99,
    "Wok": 34.99,
    "Cake Pan": 15.99,
    "Loaf Pan": 12.99,
    "Muffin Tin": 18.99,
    "Chef's Knife": 45.99,
    "Paring Knife": 14.99,
    "Bread Knife": 22.99,
    "Plates": 29.99,
    "Bowls": 24.99,
    "Glasses": 19.99,
    "Mugs": 14.99,
    "Blender": 49.99,
    "Toaster": 39.99,
    "Microwave": 89.99,
    "Food Containers": 27.99,
    "Spice Rack": 21.99,
    "Dish Rack": 18.99,
    "Dish Soap": 4.99,
    "Sponges": 3.99,
    "Microfiber Cloths": 6.99,
    "Kitchen Towels": 9.99,
    "Oven Mitts": 12.99,
    "Apron": 15.99
}

# making random receipts for one cash in one shop for a day
def generate_random_receipt():
    num_receipts = random.randint(1, 10) # how many receipts might be
    receipt_data = []
    
    for n in range(num_receipts):
        doc_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  
        num_items = random.randint(1, 5)  # how many items might be in one receipt
        
        for n in range(num_items):
            category = random.choice(list(category_items.keys()))
            item = random.choice(category_items[category])
            price = item_prices[item]
            amount = random.randint(1, 3)
            discount = round(price * (random.randint(5, 30) / 100), 2) if random.random() < 0.3 else 0

            receipt_data.append([doc_id, item, category, amount, price, discount])

    return receipt_data

os.makedirs('data', exist_ok=True)

def generate_data():
    
    for shop_num in range(1, 6):
        num_cash_registers = random.randint(1,3)

        for cash_num in range(1, num_cash_registers + 1):
            filename = f"data/{shop_num}_{cash_num}.csv"
            
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["doc_id", "item", "category", "amount", "price", "discount"])  
                receipt = generate_random_receipt()
                writer.writerows(receipt)
generate_data()