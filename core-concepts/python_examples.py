# ---------- ENCAPSULATION ----------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


# ---------- INHERITANCE ----------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


# ---------- POLYMORPHISM ----------
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


# ---------- ABSTRACTION ----------
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with a key"


if __name__ == "__main__":
    acc = BankAccount(1000)
    acc.deposit(500)
    print("Balance:", acc.get_balance())

    d = Dog("Rex")
    print(d.speak())

    for s in [Circle(5), Rectangle(4, 6)]:
        print("Area:", s.area())

    c = Car()
    print(c.start_engine())
