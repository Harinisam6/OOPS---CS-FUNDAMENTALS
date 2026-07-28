# SOLID Principles

## S — Single Responsibility Principle
A class should have only one reason to change. One job per class.

## O — Open/Closed Principle
Classes should be open for extension, closed for modification. Add new behavior via inheritance/interfaces, not by editing existing code.

## L — Liskov Substitution Principle
Subclasses should be substitutable for their base class without breaking the program.

## I — Interface Segregation Principle
Don't force a class to implement methods it doesn't use. Prefer many small interfaces over one large one.

## D — Dependency Inversion Principle
High-level modules shouldn't depend on low-level modules directly — both should depend on abstractions.

See `python_examples.py` and `java_examples.java` for a violation vs fix on each principle.
