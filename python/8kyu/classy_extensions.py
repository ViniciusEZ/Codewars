"""
The goal of this kata is to train the basic OOP concepts of inheritance and method overriding.

You will be preloaded with the Animal class, so you should only edit the Cat class.
Task

Your task is to complete the Cat class which extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

The name attribute is accessible in the class with self.name.
"""


class Animal:
    ...

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} meows."
    

cat = Cat('Mr. Whispers')

print(cat.speak())