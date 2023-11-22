"""
tests/json/test_list.py
"""
from typing import Any, Dict

import pytest

from jsonpycraft.json.list import JSONListTemplate


@pytest.fixture
def message():
    # Define a single dictionary for testing individual operations
    return {"role": "user", "content": "User message 3"}


@pytest.fixture
def messages():
    # Define a list of dictionaries for testing sequential messages
    return [
        {"role": "user", "content": "User message 1"},
        {"role": "assistant", "content": "Assistant message 1"},
        {"role": "user", "content": "User message 2"},
        {"role": "assistant", "content": "Assistant message 2"},
    ]


@pytest.fixture
def json_list_template(tmp_path, messages):
    # Create a temporary JSON file for testing
    temp_json_file = tmp_path / "test_list.json"
    temp_json_file.write_text("[]")

    # Create an instance of JSONListTemplate
    json_list = JSONListTemplate(str(temp_json_file), initial_data=messages)
    yield json_list

    # Cleanup after the test
    if temp_json_file.exists():
        temp_json_file.unlink()


def test_length(json_list_template, messages):
    assert json_list_template.length == len(messages)


def test_data(json_list_template, messages):
    assert json_list_template.data == messages


def test_append(
    json_list_template: JSONListTemplate,
    message: Dict[str, Any],
):
    initial_length = json_list_template.length
    json_list_template.append(message)
    assert json_list_template.length == initial_length + 1
    assert json_list_template.get(initial_length) == message


def test_insert(
    json_list_template: JSONListTemplate,
    message: Dict[str, Any],
):
    initial_length = json_list_template.length
    index = 1
    json_list_template.insert(index, message)
    assert json_list_template.length == initial_length + 1
    assert json_list_template.get(index) == message
    assert json_list_template.insert(-1, message) is False
    assert json_list_template.insert(initial_length + 2, message) is False


def test_get(json_list_template, messages):
    # Test getting elements at valid indices
    for index, message in enumerate(messages):
        assert json_list_template.get(index) == message

    # Test getting elements at invalid indices
    assert json_list_template.get(-1) is None
    assert json_list_template.get(len(messages)) is None


def test_update(json_list_template, message):
    # Test updating elements at valid indices
    for index in range(json_list_template.length):
        assert json_list_template.update(index, message) is True
        assert json_list_template.get(index) == message

    # Test updating elements at invalid indices
    assert json_list_template.update(-1, message) is False
    assert json_list_template.update(json_list_template.length, message) is False


def test_remove(json_list_template):
    # Test removing elements at valid indices
    for index in reversed(range(json_list_template.length)):
        assert json_list_template.remove(index) is True
        assert json_list_template.length == index

    # Verify all elements have been removed
    assert json_list_template.length == 0

    # Test removing elements at invalid indices
    assert json_list_template.remove(-1) is False
    assert json_list_template.remove(json_list_template.length) is False


def test_pop(json_list_template, messages):
    assert json_list_template.length == len(messages)
    message = json_list_template.pop(1)
    print(message)
    assert json_list_template.length == len(messages) - 1
    assert message is not None
    assert "role" in message and "content" in message
    assert message["role"] == "assistant"
    assert message["content"] == "Assistant message 1"


def test_clear(json_list_template):
    assert json_list_template.clear() is None
    assert json_list_template.data is None
