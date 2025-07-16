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