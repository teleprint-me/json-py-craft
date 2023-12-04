# JSONPyCraft Core Package

The JSONPyCraft Core Package (`jsonpycraft.core`) is a pivotal component of the JSONPyCraft project. It includes essential modules and functionalities that form the foundation for managing JSON data and implementing design patterns, with a particular emphasis on streamlined error handling and data structure management.

## Overview

The `jsonpycraft.core` package provides key components and utilities, designed to enhance the development experience when working with JSON data in Python. Key features include:

- A robust foundation for implementing the Singleton pattern.
- Custom types and comprehensive error handling related to JSON data.
- Custom exception handlers for precise error management in JSON operations.

## Modules

### Errors
- [Errors Documentation](errors.md): The Errors module contains custom exception classes specifically designed for JSON operations within the JSONPyCraft project. These include `JSONFileErrorHandler`, `JSONEncodeErrorHandler`, and `JSONDecodeErrorHandler`, each tailored for handling distinct types of JSON-related errors.

### Core Types
- [Types Documentation](types.md): The Types module defines custom types and error handling related to JSON data. It includes flexible data representation types such as `JSONMap` and `JSONList`, along with error classes like `EncodeError`, `DecodeError`, and `FileError`.

### Singleton Pattern
- [Singleton Documentation](singleton.md): The Singleton module provides the necessary base class and metaclass for implementing the Singleton design pattern, ensuring only one instance of a class exists during the application's lifecycle.

## Usage

Developers can leverage the functionalities provided by the `jsonpycraft.core` package to:

- Implement the Singleton pattern in classes where a single instance is required.
- Work with JSON data using custom types and handle various JSON-related errors efficiently.
- Manage errors in JSON operations with precision, using custom exception handlers.

## Getting Started

To begin using the JSONPyCraft Core Package, import the necessary modules and classes into your Python project:

```python
from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import JSONMap, JSONList, EncodeError, DecodeError, FileError
from jsonpycraft.core.errors import JSONFileErrorHandler, JSONEncodeErrorHandler, JSONDecodeErrorHandler
# Additional imports as needed
```

For detailed instructions and examples, refer to the documentation for each module.
