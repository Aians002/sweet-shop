from sweet import Sweet
from shop import Shop

def main():
    shop = Shop()
    while True:
        print("\nSweet Shop Management System")
        print("1. Add Sweet")
        print("2. Delete Sweet")
        print("3. View Sweets")
        print("4. Search Sweets")
        print("5. Sort Sweets")
        print("6. Purchase Sweet")
        print("7. Restock Sweet")
        print("8. Exit")
        choice = input("Enter choice (1-8): ")

        try:
            if choice == "1":
                id = int(input("Enter Sweet ID: "))
                name = input("Enter Sweet Name: ")
                category = input("Enter Category: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                shop.add_sweet(Sweet(id, name, category, price, quantity))
                print("Sweet added successfully!")
            elif choice == "2":
                id = int(input("Enter Sweet ID to delete: "))
                shop.delete_sweet(id)
                print("Sweet deleted successfully!")
            elif choice == "3":
                sweets = shop.view_sweets()
                if not sweets:
                    print("No sweets available.")
                for sweet in sweets:
                    print(f"ID: {sweet.id}, Name: {sweet.name}, Category: {sweet.category}, Price: {sweet.price}, Quantity: {sweet.quantity}")
            elif choice == "4":
                name = input("Enter Name (or press Enter to skip): ") or None
                category = input("Enter Category (or press Enter to skip): ") or None
                min_price = input("Enter Min Price (or press Enter to skip): ")
                min_price = float(min_price) if min_price else None
                max_price = input("Enter Max Price (or press Enter to skip): ")
                max_price = float(max_price) if max_price else None
                results = shop.search_sweets(name, category, min_price, max_price)
                if not results:
                    print("No sweets found.")
                for sweet in results:
                    print(f"ID: {sweet.id}, Name: {sweet.name}, Category: {sweet.category}, Price: {sweet.price}, Quantity: {sweet.quantity}")
            elif choice == "5":
                by = input("Sort by (price/name): ")
                sweets = shop.sort_sweets(by)
                if not sweets:
                    print("No sweets available.")
                for sweet in sweets:
                    print(f"ID: {sweet.id}, Name: {sweet.name}, Category: {sweet.category}, Price: {sweet.price}, Quantity: {sweet.quantity}")
            elif choice == "6":
                id = int(input("Enter Sweet ID to purchase: "))
                quantity = int(input("Enter Quantity to purchase: "))
                shop.purchase_sweet(id, quantity)
                print("Purchase successful!")
            elif choice == "7":
                id = int(input("Enter Sweet ID to restock: "))
                quantity = int(input("Enter Quantity to restock: "))
                shop.restock_sweet(id, quantity)
                print("Restock successful!")
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()