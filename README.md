# System-Management-Products
# Product Management System.

## Description.
This Python script allows you to manage a product inventory. 
It allows you to add products with name, price, and quantity, display all products, search for a product by name, update existing product information, and exit the program. 
It uses a list of dictionaries to store product information.

## Requirements.
- Python 3 installed on the system.

## Usage.
1. Run the script `activity_2.py` in a Python environment.
2. Select an option from the menu (1-5).
3. To add a product: Enter the name, price, and quantity.
4. To display products: All products in the inventory are listed.
5. To search for a product: Enter the name to search for.
6. To update a product: Enter the name and the new price and quantity.
7. Select 5 to exit.

## Main Functions.
- `add_product()`: Adds a new product to the inventory with validations.
- `show_products()`: Shows all products in the inventory.
- `search_product()`: Searches for a product by name (case insensitive).
- `update_product()`: Updates the price and quantity of an existing product.
- `main()`: Main function that manages the interactive menu.

## Example of Execution.

```
Product Management Menu
1. Add Product
2. Display Products
3. Search for Product
4. Update Product
5. Exit

Select an option (1-5): 1
Enter the product name: Laptop
Enter the product price: 1500
Enter the product quantity: 10
Product successfully added.

Select an option (1-5): 2
1. Name: Laptop, Price: 1500, Quantity: 10

Select an option (1-5): 5
Exiting the product management system.
```

## Validations.
- Product name cannot be empty.
- Price and quantity must be valid integers.
- If a product is not found when searching or updating, the user is notified.
- Menu options must be between 1 and 5.

## Notes.
- Data is stored in memory and is lost when the program is closed.
- Does not include data persistence in files.
- Search and update are not case sensitive in the name.
- Code commented to explain each section.