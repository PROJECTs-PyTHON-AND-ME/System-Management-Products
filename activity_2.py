# Product Inventory Management System:
products = []

def add_product(): # Function to add products to inventory.
    name = input("Product name: ").strip()
    if not name:
        print("Empty name. Operation canceled.\n")
        return
    
    try:
        price = float(input("Price: ").strip())
        if price < 0:
            print("The price cannot be negative.\n")
            return

        quantity = int(input("Quantity in stock: ").strip())
        if quantity < 0:
            print("The quantity cannot be negative.\n")
            return

    except ValueError:
        print("You must enter valid numbers.\n")
        return

    # Check if the product already exists (avoid duplicates by name)
    for prod in products:
        if prod["name"].lower() == name.lower():
            print(f"There is already a product with that name'{name}'.\n")
            return

    product = {
        "name": name,
        "price": round(price, 2),   
        "quantity": quantity
    }
    products.append(product)
    print(f"→ Product '{name}' successfully added.\n")

# List of dictionaries to store, search, and update products.
def show_products(): # Function to show all products in inventory.
    if not products:
        print("The inventory is empty.\n")
        return

    print("\n" + "═" * 60)
    print(f"{'#':>3}  {'Name':<25}  {'Price':>10}  {'Stock':>8}")
    print("═" * 60)

    for i, prod in enumerate(products, 1):
        print(f"{i:>3}. {prod['name']:<25}  ${prod['price']:>9.2f}  {prod['quantity']:>8}")

    print("═" * 60)
    print(f"Total products: {len(products)}\n")

def search_product(): # Function to search for a product by name.
    name = input("Name of product to search for: ").strip()
    if not name:
        print("Name empty.\n")
        return

    found = False
    for prod in products:
        if name.lower() in prod["name"].lower():
            print(f"  → {prod['name']:<25}  Precio: ${prod['price']:.2f}  Stock: {prod['quantity']}")
            found = True

    if not found:
        print("No matching products were found.\n")
    else:
        print()

def update_product(): # Function to update an existing product.
    name = input("Name of the product to be modified: ").strip()
    if not name:
        print("Name empty.\n")
        return

    for prod in products:
        if prod["name"].lower() == name.lower():
            print(f"\nProduct found: {prod['name']}")
            print(f"Current price: ${prod['price']:.2f} | Current stock: {prod['quantity']}\n")

            try:
                new_price_input = input("New price (Enter to keep): ").strip()
                new_price = prod["price"] if not new_price_input else float(new_price_input)

                new_qty_input = input("New amount (Enter to keep): ").strip()
                new_qty = prod["quantity"] if not new_qty_input else int(new_qty_input)

                if new_price < 0 or new_qty < 0:
                    print("Negative values are not allowed.\n")
                    return

                prod["price"] = round(new_price, 2)
                prod["quantity"] = new_qty
                print(f"→ Product '{prod['name']}' successfully added.\n")
                return

            except ValueError:
                print("Invalid value. Update canceled.\n")
                return

    print("Product not found.\n")


def delete_product(): # Function to delete a product from inventory.
    name = input("Product name to be delete: ").strip()
    if not name:
        print("Name empty.\n")
        return

    for i, prod in enumerate(products):
        if prod["name"].lower() == name.lower():
            confirm = input(f"Delete '{prod['name']}'? (s/n): ").strip().lower()
            if confirm in ('s', 'si', 'y', 'yes'):
                del products[i]
                print(f"Product '{prod['name']}' ddelte.\n")
            else:
                print("Operation canceled.\n")
            return

    print("Product not found.\n")

def show_menu(): # Function to display the main menu.
    print("INVENTORY SYSTEM")
    print("  1. Add product")
    print("  2. View all products")
    print("  3. Search for product")
    print("  4. Update product")
    print("  5. Delete product")
    print("  6. Exit")

def main(): # Main function to run the inventory management system.
    while True:
        show_menu()
        option = input("Select an option (1-6): ").strip()

        if option == "1":
            add_product()
        elif option == "2":
            show_products()
        elif option == "3":
            search_product()
        elif option == "4":
            update_product()
        elif option == "5":
            delete_product()
        elif option == "6":
            print("\nThank you for using the system. See you later!\n")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__": 
    main()  # Call to main function to start the program.