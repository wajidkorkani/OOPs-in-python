# OOPs-in-python

This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python, focusing on encapsulation using a `Person` class.

## Features
- **Encapsulation**: Private attributes with getter and setter methods
- **Constructor**: Default and parameterized initialization
- **Methods**: Custom methods for interaction
- **Error Handling**: Validation in setters

## Example Usage
```python
person1 = Person("Alice", 30)
print(person1.greet())  # Hello, my name is Alice and I am 30 years old.

person2 = Person()
print(person2.greet())  # Hello, my name is John and I am 49 years old.

person2.set_name("Bob")
person2.set_age(40)
print(person2.greet())  # Hello, my name is Bob and I am 40 years old.
```

## Encapsulation
- Attributes `__name` and `__age` are private.
- Access and modification are only possible through getter and setter methods.
- Direct access to private attributes (e.g., `person2.__name`) will raise an error.

## How to Run
1. Make sure you have Python installed.
2. Run the script:
   ```sh
   python index.py
   ```

## Output
```
Hello, my name is Alice and I am 30 years old.
Hello, my name is John and I am 49 years old.
Hello, my name is Bob and I am 40 years old.
```

---

Feel free to modify the `Person` class to explore more OOP concepts like inheritance and polymorphism!
# OOPs-in-python