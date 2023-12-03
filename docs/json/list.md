# JSONListTemplate Class

The `JSONListTemplate` class is part of the JSON-Py-Craft library and serves as a template for managing a list of dictionaries in JSON files. It is designed to simplify the process of working with JSON data stored in a sequence of dictionaries, providing methods for common operations such as appending, inserting, updating, and removing items from the list. This class inherits from `JSONBaseTemplate`, which provides the underlying functionality for working with JSON files.

## Class Hierarchy

- `JSONBaseTemplate` (Inherits from)
  - `JSONListTemplate`

## Constructor

### `JSONListTemplate(file_path: str, initial_data: Optional[JSONList] = None)`

- Initializes a new `JSONListTemplate` instance.
- Parameters:
  - `file_path` (str): The path to the JSON file that stores the list.
  - `initial_data` (Optional[JSONList]): Optional initial data to populate the list.

## Properties

### `length`

- Returns the length of the internal data list.

### `data`

- Returns a copy of the internal data list or None if the list is empty.

## Methods

### `append(item: JSONMap) -> None`

- Appends a dictionary to the internal data list.
- Parameters:
  - `item` (JSONMap): The dictionary to append to the internal list.

### `insert(index: int, item: JSONMap) -> bool`

- Inserts a dictionary at a specific index in the list.
- Parameters:
  - `index` (int): The index at which to insert the dictionary.
  - `item` (JSONMap): The dictionary to insert.
- Returns:
  - `bool`: True if the insertion is successful, False otherwise.

### `get(index: int) -> Optional[JSONMap]`

- Retrieves a dictionary from a specific index in the list.
- Parameters:
  - `index` (int): The index of the dictionary to retrieve.
- Returns:
  - `Optional[JSONMap]`: The dictionary at the specified index or None if the index is out of range.

### `update(index: int, item: JSONMap) -> bool`

- Updates a dictionary at a specific index in the list.
- Parameters:
  - `index` (int): The index of the dictionary to update.
  - `item` (JSONMap): The dictionary with updated values.
- Returns:
  - `bool`: True if the update is successful, False otherwise.

### `remove(index: int) -> bool`

- Removes a dictionary from a specific index in the list.
- Parameters:
  - `index` (int): The index of the dictionary to remove.
- Returns:
  - `bool`: True if the removal is successful, False otherwise.

### `pop(index: int) -> Optional[JSONMap]`

- Removes and returns a dictionary from a specific index in the list.
- Parameters:
  - `index` (int): The index of the dictionary to pop.
- Returns:
  - `Optional[JSONMap]`: The removed dictionary if successful, None otherwise.

### `clear() -> None`

- Clears the internal data list, making it empty.

## Example Usage

```python
from jsonpycraft.json.list import JSONListTemplate

# Create a JSONListTemplate instance
json_list_template = JSONListTemplate("data.json")

# Append a dictionary to the list
json_list_template.append({"name": "Alice", "age": 30})

# Insert a dictionary at a specific index
json_list_template.insert(0, {"name": "Bob", "age": 25})

# Retrieve a dictionary from the list
item = json_list_template.get(1)

# Update a dictionary in the list
json_list_template.update(0, {"name": "Charlie", "age": 28})

# Remove a dictionary from the list
json_list_template.remove(1)

# Pop a dictionary from the list
popped_item = json_list_template.pop(0)

# Clear the list
json_list_template.clear()
```
