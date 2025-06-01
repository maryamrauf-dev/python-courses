class animals:
    pass

class pet(animals):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("Wooo Wooo")

d=dog()
d.bark()