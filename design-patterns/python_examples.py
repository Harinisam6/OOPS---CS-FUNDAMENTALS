# ---------- SINGLETON ----------
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True — same instance


# ---------- FACTORY ----------
class CreditCardPayment:
    def pay(self, amount):
        return f"Paid {amount} via Credit Card"

class UPIPayment:
    def pay(self, amount):
        return f"Paid {amount} via UPI"

class PaymentFactory:
    @staticmethod
    def get_payment_method(method_type):
        if method_type == "credit_card":
            return CreditCardPayment()
        elif method_type == "upi":
            return UPIPayment()
        raise ValueError("Unknown payment method")

payment = PaymentFactory.get_payment_method("upi")
print(payment.pay(500))


# ---------- OBSERVER ----------
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_all(self, event):
        for obs in self._observers:
            obs.update(event)

class EmailObserver:
    def update(self, event):
        print(f"Email notification: {event}")

class SMSObserver:
    def update(self, event):
        print(f"SMS notification: {event}")

subject = Subject()
subject.subscribe(EmailObserver())
subject.subscribe(SMSObserver())
subject.notify_all("Order shipped")


# ---------- STRATEGY ----------
class BubbleSortStrategy:
    def sort(self, data):
        return sorted(data)  # simplified for demo

class QuickSortStrategy:
    def sort(self, data):
        return sorted(data)  # simplified for demo

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

sorter = Sorter(QuickSortStrategy())
print(sorter.sort_data([5, 2, 8, 1]))
