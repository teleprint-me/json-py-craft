"""
tests/json/test_io.py
"""
import json
import os

import pytest

from jsonpycraft.json.io import dump_json, force_read_json, read_json, write_json


@pytest.fixture
def temp_json_file(tmp_path):
    file_path = tmp_path / "test.temp.json"
    data = {"test": "data"}
    write_json(file_path, data)
    yield file_path
    if file_path.exists():
        file_path.unlink()


def test_read_json(temp_json_file):
    assert read_json(temp_json_file) == {"test": "data"}


def test_dump_json(temp_json_file):
    assert dump_json(temp_json_file) == json.dumps({"test": "data"}, indent=2)


def test_write_json(temp_json_file):
    assert read_json(temp_json_file) == {"test": "data"}


def test_force_read_json(temp_json_file):
    assert force_read_json(temp_json_file, {"another": "data"}) == {"test": "data"}
    assert read_json(temp_json_file) == {"test": "data"}
