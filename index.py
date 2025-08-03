class Person:
    def __init__(self, name="John", age=49):
        self.__name = name      # private attribute
        self.__age = age        # private attribute
    
    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive number.")
    
    def greet(self):
        return f"Hello, my name is {self.__name} and I am {self.__age} years old."

# Using the encapsulated class
person1 = Person("Alice", 30)
print(person1.greet())

person2 = Person()
print(person2.greet())

# Accessing/modifying through setters and getters
person2.set_name("Bob")
person2.set_age(40)
print(person2.greet())

# Trying to access private variables directly (will raise an error)
# print(person2.__name)  # ❌ Not allowed
# print(person2.__age)   # ❌ Not allowed
