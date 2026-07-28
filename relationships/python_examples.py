# ---------- ASSOCIATION ----------
class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model

    def drive(self, driver: Driver):
        return f"{driver.name} is driving the {self.model}"

driver = Driver("Alex")
car = Car("Tesla Model 3")
print(car.drive(driver))


# ---------- AGGREGATION ----------
class Professor:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []  # can exist independently

    def add_professor(self, professor: Professor):
        self.professors.append(professor)

prof1 = Professor("Dr. Rao")
dept = Department("Computer Science")
dept.add_professor(prof1)
# prof1 still exists even if dept is deleted
del dept
print(prof1.name)  # still valid


# ---------- COMPOSITION ----------
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # Rooms created inside House — tied to its lifecycle
        self.rooms = [Room("Bedroom"), Room("Kitchen")]

    def describe(self):
        return [r.name for r in self.rooms]

house = House()
print(house.describe())
# if house is deleted, its rooms are deleted too (garbage collected)


# ---------- DEPENDENCY ----------
class PaymentGateway:
    def process(self, amount):
        return f"Processed payment of {amount}"

class Order:
    def checkout(self, amount, gateway: PaymentGateway):
        # gateway only used temporarily, not stored as a field
        return gateway.process(amount)

order = Order()
print(order.checkout(500, PaymentGateway()))
