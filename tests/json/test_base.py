"""
tests/json/test_base.py
"""

import json
import os
from pathlib import Path

import pytest

from jsonpycraft.core.errors import (
    JSONDecodeErrorHandler,
    JSONEncodeErrorHandler,
    JSONFileErrorHandler,
)
from jsonpycraft.json.base import JSONBaseTemplate


@pytest.fixture
def json_base_template(tmp_path):
    # Create a temporary JSON file for testing
    temp_json_file = tmp_path / "test.json"
    temp_json_file.write_text('{"test": "data"}')

    # Create a JSONBaseTemplate instance
    json_template = JSONBaseTemplate(str(temp_json_file))

    yield json_template

    # Cleanup after the test
    if temp_json_file.exists():
        temp_json_file.unlink()


def test_json_file_path(json_base_template):
    assert json_base_template.file_path is not None
    assert isinstance(json_base_template.file_path, Path)
    with pytest.raises(AttributeError):  # file path is immutable
        json_base_template.file_path = "tests/error.json"


def test_json_data(json_base_template):
    # Load the data to register it
    json_base_template.load_json()
    assert json_base_template.data is not None
    assert isinstance(json_base_template.data, dict)
    assert bool(json_base_template.data) is True


def test_json_loading(json_base_template):
    json_base_template.load_json()
    assert json_base_template.data.get("test") == "data"


def test_json_saving(json_base_template):
    # Saving will only register data if we pass it to the method.
    # Otherwise it simply defaults to using its internal property.
    new_data = {"new": "data"}
    json_base_template.save_json(new_data)
    json_base_template.load_json()  # Ensure the data persisted
    assert json_base_template.data == new_data


def test_json_backup(json_base_template, tmp_path):
    temp_json_backup_path = tmp_path / "test.backup.json"
    json_base_template.backup_json()
    assert temp_json_backup_path.exists() is True
    with open(json_base_template.file_path, "r") as original, open(
        temp_json_backup_path, "r"
    ) as backup:
        assert json.load(original) == json.load(backup)
    os.remove(temp_json_backup_path)  # Cleanup the backup file


def test_json_directory_creation(json_base_template, tmp_path):
    dir_path = Path(json_base_template.file_path).parent
    if dir_path.exists():
        # Remove the file first to ensure the directory is empty
        (dir_path / json_base_template.file_path.name).unlink()
        dir_path.rmdir()  # Ensure the directory doesn't exist before the test
    json_base_template.mkdir()
    assert dir_path.exists() is True


def test_loading_nonexistent_json_file():
    json_template = JSONBaseTemplate("nonexistent.json")

    # test loading
    with pytest.raises(JSONFileErrorHandler):
        json_template.load_json()

    # test backing up loaded file
    with pytest.raises(JSONFileErrorHandler):
        json_template.backup_json()


def test_saving_with_incorrect_data_type(json_base_template, tmp_path):
    new_data = {"new", "data", "set"}
    with pytest.raises(JSONEncodeErrorHandler):
        json_base_template.save_json(new_data)


def test_loading_corrupted_json_file(tmp_path):
    temp_json_file = tmp_path / "corrupted.json"
    # Write invalid JSON data (missing closing brace)
    temp_json_file.write_text('{"key": "value"')

    json_template = JSONBaseTemplate(str(temp_json_file))
    with pytest.raises(JSONDecodeErrorHandler):
        json_template.load_json()


def test_backup_creation_insufficient_permissions(tmp_path):
    restricted_dir = tmp_path / "restricted_dir"
    os.mkdir(restricted_dir)
    original_permissions = os.stat(restricted_dir).st_mode  # Store original permissions
    try:
        os.chmod(restricted_dir, 0o000)  # Restrict write permissions

        json_base_template = JSONBaseTemplate(
            str(restricted_dir / "test.json"),
            initial_data={"key": "value"},
        )

        with pytest.raises(JSONFileErrorHandler):
            json_base_template.save_json()
            json_base_template.backup_json()
    finally:
        os.chmod(restricted_dir, original_permissions)  # Reset permissions


def test_directory_creation_with_existing_file(tmp_path):
    # Create a file with the same name as the intended directory
    conflicting_file = tmp_path / "conflicting_name"
    conflicting_file.touch()  # This creates an empty file

    # Set the JSONBaseTemplate to use a path where the last component is this file
    json_template = JSONBaseTemplate(str(conflicting_file / "test.json"))

    with pytest.raises(JSONFileErrorHandler):
        json_template.mkdir()

    # Cleanup after the test
    if conflicting_file.exists():
        conflicting_file.unlink()
