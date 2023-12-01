# JSONPyCraft Core Package

The JSONPyCraft Core Package (`jsonpycraft.core`) is a critical component of the JSONPyCraft project. It encompasses essential modules and functionality that establish the core infrastructure for managing JSON data and implementing design patterns, particularly focusing on streamlined error handling and data structure management.

## Overview

The `jsonpycraft.core` package offers fundamental components and utilities tailored for an enhanced development experience when dealing with JSON data in Python. Its key features now include:

- A robust foundation for implementing the Singleton pattern.
- Custom types and comprehensive error handling related to JSON data.

## Modules

### Singleton (`jsonpycraft.core.singleton`)

The Singleton module provides the necessary base class and metaclass to implement the Singleton design pattern. This ensures that only one instance of a class exists during the application's lifecycle.

### Types (`jsonpycraft.core.types`)

The Types module is crucial for defining custom types and error handling related to JSON data. It introduces flexible data representation types like `JSONMap` and `JSONList`, and error classes such as `JSONError`, `EncodeError`, `DecodeError`, and `FileError` for managing JSON-related errors.

## Usage

Developers can utilize the functionalities provided by the `jsonpycraft.core` package to:

- Ensure specific classes adhere to the Singleton pattern as required.
- Efficiently work with JSON data using tailored types and handle various JSON-related errors.

## Getting Started

To start using the JSONPyCraft Core Package, import the required modules and classes into your Python project:

```python
from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import (
    JSONMap,
    JSONList,
    JSONError,
    EncodeError,
    DecodeError,
    FileError,
    # Other relevant imports
)
```

For detailed usage instructions and examples, refer to the documentation of each module.
