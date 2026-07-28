# ---------- S: Single Responsibility ----------
# Bad: one class handles both invoice logic and printing
class InvoiceBad:
    def calculate_total(self): pass
    def print_invoice(self): pass

# Good: split responsibilities
class Invoice:
    def calculate_total(self): pass

class InvoicePrinter:
    def print_invoice(self, invoice): pass


# ---------- O: Open/Closed ----------
class Discount:
    def apply(self, price):
        return price

class SeasonalDiscount(Discount):
    def apply(self, price):
        return price * 0.9
# New discount types extend Discount, no need to modify existing class


# ---------- L: Liskov Substitution ----------
class Bird:
    def move(self):
        return "moving"

class Sparrow(Bird):
    def move(self):
        return "flying"

# Avoid: Penguin(Bird) overriding move() to raise an error breaks substitution


# ---------- I: Interface Segregation ----------
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): pass

class AllInOnePrinter(Printer, Scanner):
    def print_doc(self): pass
    def scan_doc(self): pass
# A simple printer only implements Printer, not forced to implement scan_doc


# ---------- D: Dependency Inversion ----------
class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")

class Alert:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def trigger(self, message):
        self.notifier.send(message)
