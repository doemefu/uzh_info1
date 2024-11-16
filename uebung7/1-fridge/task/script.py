#!/usr/bin/env python3

class Fridge:
    def __init__(self):
        self.storage = []

    def store(self, item):
        self.storage.append(item)
        self.storage.sort(key=lambda tup: tup[0], reverse=False)

    def take(self, item):
        if item not in self.storage:
            raise Warning("No matching item found")
        else:
            self.storage.remove(item)
            return item

    def find(self, name):
        for item in self.storage:
            if item[1] == name:
                return item

    def take_before(self, date):
        return [self.take(item) for item in self.storage if item[0] < date]

    def __iter__(self):
        return iter(self.storage)

    def __len__(self):
        return len(self.storage)

if __name__ == '__main__':
    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))
    f.store((191118, "Milk"))
    f.store((191116, "Coffee"))
    f.take((191127, "Milch"))  # ok
    f.take((191207, "Bread"))  # fails
    f.take((9, "käse"))  # fails

    print("Items in the fridge:")
    for i in f:
        print(f"- {i[1]} ({i[0]})")


