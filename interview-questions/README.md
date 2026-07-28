# OOP Interview Questions

## Q1: What's the difference between abstract class and interface?
Abstract class can have both implemented and abstract methods, supports constructors, and a class can extend only one abstract class. Interface (pre-Java 8) had only abstract methods, no constructors, and a class can implement multiple interfaces. Java 8+ interfaces can have default/static methods, narrowing the gap.

## Q2: Why is multiple inheritance not allowed in Java but allowed in Python?
Java avoids multiple inheritance of classes to prevent the "diamond problem" (ambiguity when two parent classes have the same method). Java allows multiple interface implementation instead, since interfaces (mostly) don't carry implementation. Python allows multiple inheritance and resolves conflicts using MRO (Method Resolution Order / C3 linearization).

## Q3: What is method overloading vs overriding?
Overloading: same method name, different parameters, resolved at compile-time (compile-time polymorphism). Overriding: subclass redefines a parent method with the same signature, resolved at runtime (runtime polymorphism).

## Q4: Why prefer composition over inheritance?
Inheritance creates tight coupling — changes in the parent class can break subclasses ("fragile base class problem"). Composition is more flexible: behavior can be swapped at runtime by composing different objects, without rigid class hierarchies.

## Q5: What is the diamond problem?
When class D inherits from both B and C, and both B and C inherit from A and override the same method, D doesn't know which version to use. Java avoids this by disallowing multiple class inheritance; Python resolves it via MRO; C++ requires virtual inheritance to fix it.

## Q6: Can you achieve abstraction without abstract classes/interfaces?
Yes, partially — by exposing only public methods and hiding internal logic (naming conventions like `_private` in Python), but true abstraction with enforced contracts needs abstract classes or interfaces.

## Q7: What's the difference between `==` and `.equals()` in Java for objects?
`==` compares references (memory addresses). `.equals()` (when overridden) compares actual content/state of objects. Default `.equals()` in Object class behaves like `==` unless overridden.

## Q8: Is Python "truly" object-oriented?
Mostly yes — everything in Python is an object (even functions and classes), but it doesn't enforce strict encapsulation (no true `private` keyword, just naming convention with `_` or `__`).

## Q9: What is dynamic (late) binding vs static (early) binding?
Static binding: method call resolved at compile time (e.g., overloading, private/static methods). Dynamic binding: resolved at runtime based on actual object type (e.g., overriding via virtual method dispatch).

## Q10: Explain "has-a" vs "is-a" relationship with an example.
"Is-a" = inheritance (a `Dog` is an `Animal`). "Has-a" = composition/aggregation (a `Car` has an `Engine`). Choosing wrong can lead to poor design — e.g., making `Stack` inherit from `Vector` (is-a) is often criticized; composition (`Stack` has-a `Vector` internally) is cleaner.
