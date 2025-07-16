class Shop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        if sweet.id in self.sweets:
            raise ValueError("Sweet ID already exists")
        self.sweets[sweet.id] = sweet

    def get_sweet_by_id(self, id):
        return self.sweets.get(id)