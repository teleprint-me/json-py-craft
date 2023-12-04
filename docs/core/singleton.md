# JSONPyCraft Singletons

The `jsonpycraft/pattern/singleton.py` module provides a base class and metaclass for implementing the Singleton pattern in the JSONPyCraft project.

## Overview

The Singleton pattern ensures that only one instance of a class is created throughout the lifetime of an application. This can be useful for scenarios where a single instance of a class needs to coordinate actions across the system.

## Usage

To create a Singleton class, follow these steps:

1. **Import the Singleton Module**:

   ```python
   from jsonpycraft.pattern.singleton import Singleton
   ```

2. **Inherit the `Singleton` Base Class**:

   Create a new class that inherits from the `Singleton` base class. Ensure that subclasses do not override the `__new__` method.

   Example:

   ```python
   class MySingleton(Singleton):
       def __init__(self, data):
           self.data = data
   ```

3. **Create Instances**:

   You can create instances of your Singleton class just like regular objects. However, only one instance will exist, no matter how many times you create it.

   Example:

   ```python
   # Creating instances of MySingleton
   instance1 = MySingleton("Instance 1")
   instance2 = MySingleton("Instance 2")

   # Both instances point to the same object
   print(instance1 is instance2)  # Output: True
   print(instance1.data)  # Output: "Instance 2"
   ```

This simple example demonstrates how to use the Singleton pattern in your Python code. The `jsonpycraft/pattern/singleton.py` module provides the foundation for creating Singleton classes in the JSONPyCraft project.
