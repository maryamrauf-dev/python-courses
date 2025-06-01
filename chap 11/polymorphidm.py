class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# List of animals with different behaviors for the same method
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())
