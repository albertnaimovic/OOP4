# Task Nr.3:

# Create a class Animal with a method speak that prints "Animal can't speak"
# Create a class Dogs that inherits from Animals and overrides the speak method to print "Woof woof"
# Create a class Cats that inherits from Animals and overrides the speak method.
# But in this new method call the speak method from the Animals class using the super() function, after that print "Meow meow"


class Animal:
    def speak(self) -> str:
        print("Animal can't speak")


class Dogs(Animal):
    def speak(self) -> str:
        print("Woof woof")


class Cats(Animal):
    def speak(self) -> str:
        super().speak()
        print("Meow meow")


Dogs().speak()
Cats().speak()
