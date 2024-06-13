class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for item in items:
            if(not self.full()):
                self.items.append(item)
        pass

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        allitems = self.items
        if len(allitems) < self.limit:
            self.items.append(item)
            return True
        pass

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

        pass

    def peek(self):
        return self.items[len(self.items)]
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1 -i
        return -1
        pass
