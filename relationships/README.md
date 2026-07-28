# Object Relationships

How objects relate to each other beyond inheritance — critical for system design interviews.

## Association
A general relationship where one class uses another, but they have independent lifecycles. "Uses-a" relationship.
Example: A `Driver` drives a `Car`. Both exist independently.

## Aggregation
A "has-a" relationship where the child can exist independently of the parent. Weak ownership.
Example: A `Department` has `Professors`, but professors can exist without the department (e.g., transfer elsewhere).

## Composition
A "has-a" relationship with strong ownership — the child's lifecycle depends on the parent. If parent is destroyed, child is destroyed too.
Example: A `House` has `Rooms`. Rooms don't exist without the house.

## Dependency
A class depends on another temporarily, usually as a method parameter — weakest relationship.
Example: An `Order` class depends on a `PaymentGateway` only during checkout.

## Quick comparison

| Relationship | Ownership strength | Lifecycle dependency | Example |
|---|---|---|---|
| Association | None | Independent | Driver ↔ Car |
| Aggregation | Weak | Independent | Department → Professors |
| Composition | Strong | Dependent | House → Rooms |
| Dependency | Temporary | N/A | Order uses PaymentGateway |

## Why this matters for interviews
System design and OOP-design interview questions (e.g., "design a parking lot", "design a library system") are graded heavily on whether you pick the right relationship type between classes. Composition is generally preferred over inheritance for flexibility (see "composition over inheritance" principle).
