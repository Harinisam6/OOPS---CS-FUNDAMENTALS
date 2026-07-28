# OOP Design Patterns

Common design patterns asked about in interviews, with Python and Java implementations.

## Singleton
Ensures a class has only one instance and provides a global point of access to it.
Use case: Database connection pool, logging service.

## Factory
Creates objects without exposing the instantiation logic, using a common interface.
Use case: Creating different payment method objects (CreditCard, UPI, Wallet) based on input.

## Observer
Defines a one-to-many dependency so that when one object changes state, all dependents are notified automatically.
Use case: Event listeners, pub-sub systems, notification services.

## Strategy
Defines a family of algorithms, encapsulates each, and makes them interchangeable at runtime.
Use case: Different sorting strategies, different route-calculation algorithms.

## Quick comparison

| Pattern | Category | Solves |
|---|---|---|
| Singleton | Creational | Single shared instance |
| Factory | Creational | Flexible object creation |
| Observer | Behavioral | Event-driven updates |
| Strategy | Behavioral | Swappable algorithms at runtime |
