class Shop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        if sweet.id in self.sweets:
            raise ValueError("Sweet ID already exists")
        self.sweets[sweet.id] = sweet

    def get_sweet_by_id(self, id):
        return self.sweets.get(id)
    
    def delete_sweet(self, id):
        if id not in self.sweets:
            raise ValueError("Sweet ID does not exist")
        del self.sweets[id]

    def view_sweets(self):
        return list(self.sweets.values())
    
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
    
    def sort_sweets(self, by="price"):
        if by not in ["price", "name"]:
            raise ValueError("Sort by 'price' or 'name' only")
        return sorted(self.sweets.values(), key=lambda x: x.price if by == "price" else x.name)