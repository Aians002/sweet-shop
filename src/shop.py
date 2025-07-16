class Shop:
    def __init__(self):
        self.sweets = {} #Stores Sweets with ID as key

    #Add a new sweet
    def add_sweet(self, sweet):
        if sweet.id in self.sweets:
            raise ValueError("Sweet ID already exists") #Check for duplicate ID
        self.sweets[sweet.id] = sweet

    #Get a sweet by ID
    def get_sweet_by_id(self, id):
        return self.sweets.get(id)

    #Delete a sweet by ID
    def delete_sweet(self, id):
        if id not in self.sweets:
            raise ValueError("Sweet ID does not exist") #Check if Sweet ID exists
        del self.sweets[id]

    #View all sweets
    def view_sweets(self):
        return list(self.sweets.values())
    
    #Search sweets by various criteria
    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        results = list(self.sweets.values())
        if name:
            results = [sweet for sweet in results if name.lower() in sweet.name.lower()]
        if category:
            results = [sweet for sweet in results if sweet.category.lower() == category.lower()]
        if min_price is not None:
            results = [sweet for sweet in results if sweet.price >= min_price]
        if max_price is not None:
            results = [sweet for sweet in results if sweet.price <= max_price]
        return results
    
    #Sort sweets by price or name
    def sort_sweets(self, by="price"):
        if by not in ["price", "name"]:
            raise ValueError("Sort by 'price' or 'name' only") #Check valid sort criteria
        return sorted(self.sweets.values(), key=lambda x: x.price if by == "price" else x.name)
    
    def purchase_sweet(self, id, quantity):
        sweet = self.get_sweet_by_id(id)
        if not sweet:
            raise ValueError("Sweet ID does not exist") #Check if Sweet ID exists
        if sweet.quantity < quantity:
            raise ValueError("Insufficient stock") #Check if sufficient stock exists
        sweet.quantity -= quantity

    def restock_sweet(self, id, quantity):
        sweet = self.get_sweet_by_id(id)
        if not sweet:
            raise ValueError("Sweet ID does not exist") #Check if Sweet ID exists
        if quantity < 0:
            raise ValueError("Restock quantity cannot be negative") #Check if restock quantity is valid
        sweet.quantity += quantity