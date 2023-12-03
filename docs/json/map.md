# JSONMapTemplate Class

The `JSONMapTemplate` class is part of the JSON-Py-Craft library and serves as a template for managing a mapping of key-value pairs in JSON files. It simplifies the process of working with JSON data stored as a collection of key-value pairs, providing methods for common operations such as creating, reading, updating, and deleting items within the mapping. This class inherits from `JSONBaseTemplate`, which provides the underlying functionality for working with JSON files.

## Class Hierarchy

- `JSONBaseTemplate` (Inherits from)
  - `JSONMapTemplate`

## Constructor

### `JSONMapTemplate(file_path: str, initial_data: Optional[JSONMap] = None)`

- Initializes a new `JSONMapTemplate` instance.
- Parameters:
  - `file_path` (str): The path to the JSON file that stores the mapping.
  - `initial_data` (Optional[JSONMap]): Optional initial data to populate the mapping.

## Properties

### `keys`

- Returns a list of all keys in the mapping.

### `data`

- Returns a copy of the internal data structure representing the mapping or None if it's empty.

## Methods

### `create(key: str, value: Any) -> bool`

- Creates a new key-value pair in the mapping.
- Parameters:
  - `key` (str): The key of the pair.
  - `value` (Any): The value of the pair.
- Returns `True` if the key-value pair was created successfully, `False` if the key already exists.

### `create_nested(value: Any, *keys: str) -> bool`

- Creates a nested key-value pair in the mapping.
- Parameters:
  - `value` (Any): The value of the pair.
  - `keys` (str): The keys hierarchy for the nested pair.
- Returns `True` if the nested key-value pair was created successfully, `False` if any key in the hierarchy is missing or if the final key already exists.

### `read(key: str) -> Any`

- Reads the value associated with a key in the mapping.
- Parameters:
  - `key` (str): The key to read the value from.
- Returns the value associated with the key, or None if the key is not present in the mapping.

### `read_nested(*keys: str) -> Any`

- Reads the value associated with a nested key hierarchy in the mapping.
- Parameters:
  - `keys` (str): The keys hierarchy for the nested value.
- Returns the value associated with the nested keys hierarchy, or None if any key in the hierarchy is missing.

### `update(key: str, value: Any) -> bool`

- Updates the value associated with a key in the mapping. If the key is already present in the mapping, the value is updated. Otherwise, a new key-value pair is created.
- Parameters:
  - `key` (str): The key to update or create.
  - `value` (Any): The value to associate with the key.
- Returns `True` if the value was updated, `False` if a new key-value pair was created.

### `update_nested(value: Any, *keys: str, overwrite: bool = True) -> bool`

- Updates the value associated with a nested key hierarchy in the mapping. If the nested keys hierarchy is already present in the mapping, the value is updated. Otherwise, a new nested key-value pair is created.
- Parameters:
  - `value` (Any): The value to associate with the nested keys hierarchy.
  - `keys` (str): The keys hierarchy for the nested value.
  - `overwrite` (bool): Overwrite exiting non-empty dictionaries.

- Returns `True` if the value was updated, `False` if a new nested key-value pair was created.

### `delete(key: str) -> bool`

- Deletes a key-value pair from the mapping.
- Parameters:
  - `key` (str): The key to delete.
- Returns `True` if the key-value pair was deleted successfully, `False` if the key is not present in the mapping.

### `delete_nested(*keys: str) -> bool`

- Deletes a nested key-value pair from the mapping.
- Parameters:
  - `keys` (str): The keys hierarchy for the nested value.
- Returns `True` if the nested key-value pair was deleted successfully, `False` if any key in the hierarchy is missing.

## Example Usage

```python
# Creating an instance of JSONMapTemplate
map_template = JSONMapTemplate("data.json")

# Creating a new key-value pair
map_template.create("name", "John Doe")

# Reading the value associated with a key
name = map_template.read("name")
print(name)  # Output: "John Doe"

# Updating a key-value pair
map_template.update("name", "Jane Doe")

# Deleting a key-value pair
map_template.delete("name")
```

## Notes

- The `JSONMapTemplate` class simplifies working with structured JSON data by providing convenient methods for managing key-value pairs within the mapping.
- It can be particularly useful for applications that require structured data storage and retrieval from JSON files.
