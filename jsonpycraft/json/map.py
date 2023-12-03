"""
jsonpycraft/json/map.py
"""
from logging import Logger
from typing import Any, Optional

from jsonpycraft.core.types import JSONMap
from jsonpycraft.json.base import JSONBaseTemplate


class JSONMapTemplate(JSONBaseTemplate):
    """
    A template class for creating and managing a mapping of key-value pairs.

    Attributes:
        _file_path (Path): A path-like object pointing to the JSON source file.
        _data (Optional[JSONData]): The internal JSON data structure. May be None if not loaded.
    """

    def __init__(
        self,
        file_path: str,
        initial_data: Optional[JSONMap] = None,
    ):
        """
        Initializes the JSONMapTemplate.

        Args:
            file_path (str): The path to the JSON file.
            initial_data (Optional[JSONMap]): Optional initial data to populate the mapping.
        """
        super(JSONMapTemplate, self).__init__(file_path, initial_data)

        if initial_data is None:
            self._data = {}

    @property
    def keys(self) -> list[str]:
        """
        Get a list of all keys in the mapping.

        Returns:
            list[str]: A list of keys in the mapping.
        """
        return list(self._data.keys())

    @property
    def data(self) -> JSONMap:
        """
        Get the underlying data structure of the mapping.

        Returns:
            JSONMap: The underlying data structure.
        """
        return self._data

    def create(self, key: str, value: Any) -> bool:
        """
        Create a new key-value pair in the mapping.

        Args:
            key (str): The key of the pair.
            value (Any): The value of the pair.

        Returns:
            bool: True if the key-value pair was created successfully, False if the key already exists.
        """
        if key not in self._data:
            self._data[key] = value
            return True

        return False

    def create_nested(self, value: Any, *keys: str) -> bool:
        """
        Create a nested key-value pair in the mapping.

        Args:
            value (Any): The value of the pair.
            keys (str): The keys hierarchy for the nested pair.

        Returns:
            bool: True if the nested key-value pair was created successfully, False if any key in the hierarchy is missing or if the final key already exists.
        """
        if not keys:
            raise ValueError("At least one key is required")

        data = self._data
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if isinstance(data, dict):
                data = data.setdefault(key, {})
            else:
                return False

        if last_key not in data:
            data[last_key] = value
            return True

        return False

    def read(self, key: str) -> Any:
        """
        Read the value associated with a key in the mapping.

        Args:
            key (str): The key to read the value from.

        Returns:
            Any: The value associated with the key, or None if the key is not present in the mapping.
        """
        return self._data.get(key, None)

    def read_nested(self, *keys: str) -> Any:
        """
        Read the value associated with a nested key hierarchy in the mapping.

        Args:
            keys (str): The keys hierarchy for the nested value.

        Returns:
            Any: The value associated with the nested keys hierarchy, or None if any key in the hierarchy is missing.
        """
        if not keys:
            raise ValueError("At least one key is required")

        data = self._data
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data.get(key, None)
            else:
                return None
        return data

    def update(self, key: str, value: Any) -> bool:
        """
        Update the value associated with a key in the mapping.

        If the key is already present in the mapping, the value is updated. Otherwise, a new key-value pair is created.

        Args:
            key (str): The key to update or create.
            value (Any): The value to associate with the key.

        Returns:
            bool: True if the value was updated, False if a new key-value pair was created.
        """
        if key in self._data:
            self._data[key] = value
            return True
        else:
            return self.create(key, value)

    def update_nested(self, value: Any, *keys: str, overwrite: bool = True) -> bool:
        """
        Update the value associated with a nested key hierarchy in the mapping.

        If the nested keys hierarchy is already present in the mapping, the value is updated. Otherwise, a new nested key-value pair is created.

        Args:
            value (Any): The value to associate with the nested keys hierarchy.
            keys (str): The keys hierarchy for the nested value.
            overwrite (bool): Overwrite exiting non-empty dictionaries. Default is True.

        Returns:
            bool: True if the value was updated, False if a new nested key-value pair was created.
        """
        if not keys:
            raise ValueError("At least one key is required")

        data = self._data
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if not isinstance(key, (str, int)):
                raise TypeError(f"Key {key} is not a valid type")

            if not isinstance(data, dict):
                raise TypeError(
                    f"Intermediate key '{key}' does not lead to a dictionary"
                )

            if key not in data or not isinstance(data[key], dict) or overwrite:
                data[key] = {}

            data = data[key]

        if not isinstance(last_key, (str, int)):
            raise TypeError(f"Last key {last_key} is not a valid type")

        data[last_key] = value
        return True

    def delete(self, key: str) -> bool:
        """
        Delete a key-value pair from the mapping.

        Args:
            key (str): The key to delete.

        Returns:
            bool: True if the key-value pair was deleted successfully, False if the key is not present in the mapping.
        """
        if key in self._data:
            del self._data[key]
            return True

        return False

    def delete_nested(self, *keys: str) -> bool:
        """
        Delete a nested key-value pair from the mapping.

        Args:
            keys (str): The keys hierarchy for the nested value.

        Returns:
            bool: True if the nested key-value pair was deleted successfully, False if any key in the hierarchy is missing.
        """
        if not keys:
            raise ValueError("At least one key is required")

        data = self._data
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return False

        if isinstance(data, dict) and last_key in data:
            del data[last_key]
            return True

        return False
