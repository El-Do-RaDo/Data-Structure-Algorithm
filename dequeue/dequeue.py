class Dequeue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        self.items == []
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0, item)
    def remove_front(self):
        return self.items.pop()
    
