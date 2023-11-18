# JSONPyCraft Core Package

The JSONPyCraft Core Package (`jsonpycraft.core`) is a fundamental component of the JSONPyCraft project. This package contains essential modules and functionality that form the core infrastructure for managing JSON data, implementing design patterns, and handling errors.

## Overview

The `jsonpycraft.core` package provides key components and utilities designed to enhance the development experience when working with JSON data in Python. It includes:

- Logging utilities for efficient and configurable logging.
- A foundation for implementing the Singleton pattern.
- Custom types and error handling related to JSON data.

## Modules

### Logger (`jsonpycraft.core.logger`)

The Logger module offers a flexible and configurable logging utility. It allows developers to create and customize logger instances, making it easier to track and manage application events.

### Singleton (`jsonpycraft.core.singleton`)

The Singleton module provides the necessary base class and metaclass to implement the Singleton design pattern. This pattern ensures that only one instance of a class is created throughout the application's lifetime.

### Types (`jsonpycraft.core.types`)

The Types module defines custom types and error handling related to JSON data. It introduces types such as `JSONMap` and `JSONList` for flexible data representation and error classes like `JSONError` for handling JSON-related errors.

## Usage

Developers can leverage the functionalities provided by the `jsonpycraft.core` package to:

- Implement efficient and customizable logging in their applications.
- Ensure that specific classes follow the Singleton pattern when necessary.
- Work with JSON data using custom types and handle JSON-related errors effectively.

## Getting Started

To get started with the JSONPyCraft Core Package, simply import the relevant modules and classes into your Python code:

```python
from jsonpycraft.core import logger
from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import (
    JSONMap,
    JSONList,
    JSONError,
    # Add other imports as needed
)
```

Refer to the respective module's documentation for detailed usage instructions and examples.
