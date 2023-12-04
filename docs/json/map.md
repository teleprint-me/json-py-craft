# JSONMapTemplate Class

The `JSONMapTemplate` class is part of the JSON-Py-Craft library and serves as a template for managing a mapping of key-value pairs in JSON files. It simplifies the process of working with JSON data stored as a collection of key-value pairs, providing methods for common operations such as creating, reading, updating, and deleting items within the mapping. This class inherits from `JSONBaseTemplate`, which provides the underlying functionality for working with JSON files.

## Class Hierarchy

- `JSONBaseTemplate` (Inherits from)
  - `JSONMapTemplate`

## Constructor

### JSONMapTemplate(file_path: str, initial_data: Optional[JSONMap] = None)

- Initializes a new `JSONMapTemplate` instance.
- Parameters:
  - `file_path` (str): The path to the JSON file that stores the mapping.
  - `initial_data` (Optional[JSONMap]): Optional initial data to populate the mapping.

## Properties

### keys

- Returns a list of all keys in the mapping.

### data

- Returns a copy of the internal data structure representing the mapping or None if it's empty.

## Methods

### create(key: str, value: Any) -> bool

- Creates a new key-value pair in the mapping.
- Parameters:
  - `key` (str): The key of the pair.
  - `value` (Any): The value of the pair.
- Returns `True` if the key-value pair was created successfully, `False` if the key already exists.

### create_nested(value: Any, *keys: str) -> bool

- Creates a nested key-value pair in the mapping.
- Parameters:
  - `value` (Any): The value of the pair.
  - `keys` (str): The keys hierarchy for the nested pair.
- Returns `True` if the nested key-value pair was created successfully, `False` if any key in the hierarchy is missing or if the final key already exists.

### read(key: str) -> Any

- Reads the value associated with a key in the mapping.
- Parameters:
  - `key` (str): The key to read the value from.
- Returns the value associated with the key, or None if the key is not present in the mapping.

### read_nested(*keys: str) -> Any

- Reads the value associated with a nested key hierarchy in the mapping.
- Parameters:
  - `keys` (str): The keys hierarchy for the nested value.
- Returns the value associated with the nested keys hierarchy, or None if any key in the hierarchy is missing.

### update(key: str, value: Any) -> bool

- Updates the value associated with a key in the mapping. If the key is already present in the mapping, the value is updated. Otherwise, a new key-value pair is created.
- Parameters:
  - `key` (str): The key to update or create.
  - `value` (Any): The value to associate with the key.
- Returns `True` if the value was updated, `False` if a new key-value pair was created.

### update_nested(value: Any, *keys: str, overwrite: bool = True) -> bool

- Updates the value associated with a nested key hierarchy in the mapping. If the nested keys hierarchy is already present in the mapping, the value is updated. Otherwise, a new nested key-value pair is created.
- Parameters:
  - `value` (Any): The value to associate with the nested keys hierarchy.
  - `keys` (str): The keys hierarchy for the nested value.
  - `overwrite` (bool): Determines whether to overwrite existing non-empty dictionaries at any level of the specified key hierarchy. When `True`, existing dictionaries are overwritten; when `False`, they are preserved.
- Returns:
  - `bool`: Always returns `True` upon successful update or creation.

### delete(key: str) -> bool

- Deletes a key-value pair from the mapping.
- Parameters:
  - `key` (str): The key to delete.
- Returns `True` if the key-value pair was deleted successfully, `False` if the key is not present in the mapping.

### delete_nested(*keys: str) -> bool

- Deletes a nested key-value pair from the mapping.
- Parameters:
  - `keys` (str): The keys hierarchy for the nested value.
- Returns `True` if the nested key-value pair was deleted successfully, `False` if any key in the hierarchy is missing.

## Example Usage

### Scenario

Developing an application requiring management of user profiles with various preferences, including notification settings, stored in a JSON file.

### 1. Initialize `JSONMapTemplate` and Load Data:

```python
from jsonpycraft.json.map import JSONMapTemplate
from jsonpycraft.core.errors import JSONFileErrorHandler, JSONDecodeErrorHandler

user_profiles = JSONMapTemplate("user_profiles.json")

try:
    user_profiles.load_json()
    print("Existing data loaded:", user_profiles.data)
except JSONFileErrorHandler as e:
    print(f"File access error for {user_profiles.file_path}: {e}")
except JSONDecodeErrorHandler as e:
    print(f"JSON decoding error: {e}")
```

### 2. Create Nested Structure for User Preferences:

```python
user_profiles.create_nested({"notifications": False}, "Alice", "preferences")
```

### 3. Add Root-Level User Profile:

```python
if not user_profiles.create("Alice", {"email": "alice@example.com", "age": 30}):
    print("Alice already exists. Profile not overwritten.")
```

### 4. Overwrite Protection:

```python
if not user_profiles.create("Alice", {"email": "alice2@example.com"}):
    print("Attempted overwrite blocked.")
```

### 5. Read Data Safely:

```python
preferences = user_profiles.read_nested("Alice", "preferences")
if preferences is not None:
    print("Alice's preferences:", preferences)

alice_profile = user_profiles.read("Alice")
email = alice_profile.get("email") if alice_profile else None
print("Alice's email:", email if email else "Not available")
```

### 6. Update Nested Key-Value Pair:

```python
user_profiles.update_nested(True, "Alice", "preferences", "notifications")
```

### 7. Delete Key-Value Pair:

```python
if user_profiles.delete("Alice"):
    print("Alice's profile deleted.")
else:
    print("Alice's profile not found.")

print("Current data:", user_profiles.data)
```

### 8. Save Modified Data:

```python
from jsonpycraft.core.errors import JSONEncodeErrorHandler

try:
    user_profiles.save_json()
    print("Data saved successfully.")
except JSONFileErrorHandler as e:
    print(f"Error saving to {user_profiles.file_path}: {e}")
except JSONEncodeErrorHandler as e:
    print(f"JSON encoding error: {e}")
```

## Conclusion

The `JSONMapTemplate` class in JSONPyCraft provides a structured and versatile approach for managing JSON data, useful for applications like user profile management. It offers robust error handling, ensuring data integrity and smooth operation under various conditions.

It simplifies working with structured JSON data by providing convenient methods for managing key-value pairs within the mapping. This makes it particularly useful for applications that require structured data storage and retrieval from JSON files.
