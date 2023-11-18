"""
jsonpycraft/pattern/singleton.py

This module provides a base class and metaclass for implementing the Singleton pattern.

The Singleton pattern ensures that only one instance of a class is created throughout the lifetime of an application.

Example Usage:
    from jsonpycraft.pattern.singleton import Singleton

    class MySingleton(Singleton):
        def __init__(self, data):
            self.data = data

    # Creating instances of MySingleton
    instance1 = MySingleton("Instance 1")
    instance2 = MySingleton("Instance 2")

    # Both instances point to the same object
    print(instance1 is instance2)  # Output: True
    print(instance1.data)  # Output: "Instance 2"

Note:
- Subclasses should not override the `__new__` method.
"""


class MetaSingleton(type):
    """
    Metaclass for implementing the Singleton pattern.

    Attributes:
        _instances (dict): A dictionary storing the singleton instances of classes.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Call method invoked when a singleton class is instantiated.

        Args:
            cls (type): The class object.

        Returns:
            object: The singleton instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(object, metaclass=MetaSingleton):
    """
    Base class for implementing the Singleton pattern.

    This class should be inherited by classes that need to be singletons.

    Note:
        Subclasses should not override the __new__ method.

    Attributes:
        None
    """

    def __init__(self):
        """
        Initializes a new instance of the Singleton class.

        Note:
            This method is where initialization should be performed.
        """
        super(Singleton, self).__init__()
