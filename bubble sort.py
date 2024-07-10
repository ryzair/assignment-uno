import os
import time

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
    def __repr__(self):
        return f"Product(ID: {self.id}, Name: {self.name}, Price: {self.price}, Category: {self.category})"

# Task 1: Data Management Using Fundamental Structures

def load_data(file_path):
    products = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                id = int(parts[0])
                name = parts[1]
                price = float(parts[2])
                category = parts[3]
                products.append(Product(id, name, price, category))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return products

# Task 2: Data Manipulation Operations

def insert_product(products, new_product):
    products.append(new_product)

def update_product(products, id, new_name, new_price, new_category):
    for product in products:
        if product.id == id:
            product.name = new_name
            product.price = new_price
            product.category = new_category
            break

def delete_product(products, id):
    products[:] = [product for product in products if product.id != id]

def search_product_by_id(products, id):
    for product in products:
        if product.id == id:
            return product
    return None

# Task 3: Sorting Algorithm Implementation (Bubble Sort)

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]
                swapped = True
        if not swapped:
            break

# Task 4: Complexity Analysis

def measure_sorting_time(sort_func, products):
    start_time = time.time()  # Start measuring time
    sort_func(products)
    end_time = time.time()  # Stop measuring time
    return end_time - start_time  # Calculate elapsed time

# Function to display menu and handle user commands
def display_menu():
    print("\nMenu:")
    print("1. Insert a Product")
    print("2. Update a Product")
    print("3. Delete a Product")
    print("4. Search for a Product by ID")
    print("5. Sort Products by Price (Bubble Sort)")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

# Main execution
if __name__ == "__main__":
    # Determine script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "product_data.txt")
    
    # Print current working directory and resolved file path for debugging
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    
    # Load data
    product_data = load_data(file_path)
    
    if product_data:
        while True:
            choice = display_menu()

            if choice == '1':
                id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                category = input("Enter Product Category: ")
                insert_product(product_data, Product(id, name, price, category))
                print("Product inserted successfully.")

            elif choice == '2':
                id = int(input("Enter Product ID to update: "))
                new_name = input("Enter New Name: ")
                new_price = float(input("Enter New Price: "))
                new_category = input("Enter New Category: ")
                update_product(product_data, id, new_name, new_price, new_category)
                print("Product updated successfully.")

            elif choice == '3':
                id = int(input("Enter Product ID to delete: "))
                delete_product(product_data, id)
                print("Product deleted successfully.")

            elif choice == '4':
                id = int(input("Enter Product ID to search: "))
                result = search_product_by_id(product_data, id)
                if result:
                    print("Product found:")
                    print(result)
                else:
                    print("Product not found.")

            elif choice == '5':
                print("Sorting products by price using Bubble Sort...")
                bubble_sort(product_data)
                print("Products sorted successfully.")

                # Print sorted data
                print("\nSorted Products by Price:")
                for product in product_data:
                    print(product)
                
                # Measure time complexity
                bubble_sorted_time = measure_sorting_time(bubble_sort, product_data)
                print(f"\nBubble Sort Time: {bubble_sorted_time:.6f} seconds")

            elif choice == '6':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
