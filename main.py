from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Dragon's Breath"
owner_name = "Kelly Pangilinan"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Steak", "Roasted Chicken", "Mashed Poatatoes"]
beverages = ["Beer", "Ale"]

# Tuple data type
business_hours = ("07:00 PM", "04:00 AM")

# Dictionary data type
menu = {
    "Steak": 270.00,
    "Roasted Chicken": 170.00,
    "Mashed Potatoes": 80.00,
    "Beer": 80.00,
    "Ale": 75.00
}

# Set data type
common_allergens = {"gluten", "dairy","yeast","barley"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Steak']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Roasted Chicken']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Mashed Potatoes']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Beer']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Ale']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")

