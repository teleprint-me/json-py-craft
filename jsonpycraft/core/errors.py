"""
jsonpycraft/core/errors.py

Custom Exceptions for JSON Operations

This module defines custom exception classes for handling errors related to JSON operations within the jsonpycraft library. These exceptions can be used to capture and handle specific error scenarios that may occur during JSON encoding, decoding, or file-related operations.

Exception Classes:
- JSONFileErrorHandler: Exception raised for file-related errors in JSON operations.
- JSONEncodeErrorHandler: Exception raised for errors during JSON encoding.
- JSONDecodeErrorHandler: Exception raised for errors during JSON decoding.

Usage:
You can use these custom exceptions in your jsonpycraft-based applications to provide more detailed error messages or to handle specific error conditions gracefully. When a relevant error occurs, you can raise one of these exceptions, and in your code, you can catch and handle them as needed.
"""


class JSONFileErrorHandler(Exception):
    """Exception raised for file-related errors in JSON operations."""

    pass


class JSONEncodeErrorHandler(Exception):
    """Exception raised for errors during JSON encoding."""

    pass


class JSONDecodeErrorHandler(Exception):
    """Exception raised for errors during JSON decoding."""

    pass


# Additional custom exceptions can be added here as needed.
