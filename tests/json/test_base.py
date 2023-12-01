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
    json_base_template.make_directory()
    assert dir_path.exists() is True
