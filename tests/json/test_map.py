"""
tests/json/test_map.py
"""
import pytest

from jsonpycraft.core.types import JSONMap
from jsonpycraft.json.map import JSONMapTemplate


@pytest.fixture(scope="function")
def temp_map_data() -> JSONMap:
    return {"key1": "value1", "nested": {"key2": "value2"}}


@pytest.fixture(scope="function")
def json_map_template(tmp_path, temp_map_data) -> JSONMapTemplate:
    """
    Pytest fixture to create an instance of JSONMapTemplate for testing.

    Args:
        tmp_path: Pytest built-in fixture for creating temporary directories.

    Returns:
        JSONMapTemplate: An instance of JSONMapTemplate.
    """
    # Create a temporary JSON file for testing
    temp_json_file = tmp_path / "test_map.json"
    temp_json_file.write_text("{}")

    # Create an instance of JSONMapTemplate
    json_map = JSONMapTemplate(str(temp_json_file), initial_data=temp_map_data)
    yield json_map

    # Cleanup after the test
    if temp_json_file.exists():
        temp_json_file.unlink()


def test_create(json_map_template):
    # Create a new key-value pair
    assert json_map_template.create("new_key", "new_value") is True

    # Attempt to create the same key-value pair again (should return False since it already exists)
    assert json_map_template.create("new_key", "new_value") is False

    # Check existing key-value pair
    assert json_map_template.data["new_key"] == "new_value"


def test_create_nested(json_map_template):
    assert json_map_template.create_nested("new_value", "nested", "key3") is True
    assert json_map_template.data["nested"]["key3"] == "new_value"


def test_read(json_map_template):
    assert json_map_template.read("key1") == "value1"


def test_read_nested(json_map_template):
    assert json_map_template.read_nested("nested", "key2") == "value2"


def test_update(json_map_template):
    assert json_map_template.update("key1", "updated_value") is True
    assert json_map_template.data["key1"] == "updated_value"


def test_update_nested(json_map_template):
    assert json_map_template.update_nested("updated_value", "nested", "key2") is True
    assert json_map_template.data["nested"]["key2"] == "updated_value"


def test_delete(json_map_template):
    assert json_map_template.delete("key1") is True
    assert "key1" not in json_map_template.data


def test_delete_nested(json_map_template):
    assert json_map_template.delete_nested("nested", "key2") is True
    assert "key2" not in json_map_template.data["nested"]


def test_create_existing_key(json_map_template):
    # Ensure that 'create' does not overwrite an existing key
    original_value = json_map_template.read("key1")
    assert json_map_template.create("key1", "new_value") is False
    assert json_map_template.read("key1") == original_value


def test_read_nonexistent_key(json_map_template):
    # Read should return None for a nonexistent key
    assert json_map_template.read("nonexistent_key") is None


def test_read_nested_nonexistent_key(json_map_template):
    # Read nested should return None for a nonexistent nested key
    assert json_map_template.read_nested("nested", "nonexistent_key") is None


def test_update_and_create_behavior(json_map_template):
    # Update existing key
    assert json_map_template.update("new_key", "updated_value") is True
    assert json_map_template.read("new_key") == "updated_value"

    # Create new key
    assert json_map_template.update("nonexistent_key", "new_value") is True
    assert json_map_template.read("nonexistent_key") == "new_value"


def test_update_nested_nonexistent_key(json_map_template):
    assert (
        json_map_template.update_nested("new_value", "nested", "nonexistent_key")
        is True
    )


def test_delete_nonexistent_key(json_map_template):
    # Delete should return False for a nonexistent key
    assert json_map_template.delete("nonexistent_key") is False


def test_delete_nested_nonexistent_key(json_map_template):
    # Delete nested should return False for a nonexistent nested key
    assert json_map_template.delete_nested("nested", "nonexistent_key") is False


def test_nested_operations_with_non_dict(json_map_template):
    # Setup: Create a non-dict key
    json_map_template.create("non_dict_key", "non_dict_value")

    # Test nested read on non-dict key
    assert json_map_template.read_nested("non_dict_key", "key") is None

    # Test nested update on non-dict key
    assert json_map_template.update_nested("new_value", "non_dict_key", "key") is True

    # Test nested delete on non-dict key
    assert json_map_template.delete_nested("non_dict_key", "key") is True
