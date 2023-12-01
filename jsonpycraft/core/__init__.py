"""
jsonpycraft/core/__init__.py
"""
from jsonpycraft.core.errors import (
    JSONDecodeErrorHandler,
    JSONEncodeErrorHandler,
    JSONFileErrorHandler,
)
from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import (
    DecodeError,
    EncodeError,
    FileError,
    JSONData,
    JSONError,
    JSONList,
    JSONMap,
)
