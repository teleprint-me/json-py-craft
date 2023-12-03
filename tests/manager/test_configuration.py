"""
tests/manager/test_configuration.py
"""

import pytest

from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import JSONMap
from jsonpycraft.json.map import JSONMapTemplate
from jsonpycraft.manager.configuration import ConfigurationManager


# Fixture to create a mock configuration data structure for testing
@pytest.fixture(scope="function")
def mock_config() -> JSONMap:
    return {
        "home": {
            "path": "${HOME}/.local",
            "type": "dir",
        },
        "app": {
            "provider": "jsonpycraft",
            "local": {"path": "tests/local", "type": "dir"},
            "env": {"path": "tests/local/env", "type": "file"},
            "logs": {
                "general": {
                    "path": "tests/local/logs/general.log",
                    "level": "INFO",
                    "type": "file",
                },
            },
        },
    }


# Fixture to create a ConfigurationManager instance for testing
@pytest.fixture(scope="function")
def config_manager(tmp_path, mock_config) -> ConfigurationManager:
    # Create a temporary JSON configuration file
    config_file = tmp_path / "test_config.json"
    config_file.write_text("{}")

    print("mock config:", mock_config)

    # Create an instance of ConfigurationManager
    config = ConfigurationManager(str(config_file), initial_data=mock_config)

    yield config

    # Cleanup after the test
    if config_file.exists():
        config_file.unlink()

    # Teardown step to reset Singleton instance
    ConfigurationManager._instances = {}


def test_types(config_manager: ConfigurationManager):
    assert isinstance(config_manager, Singleton)
    assert isinstance(config_manager, ConfigurationManager)


def test_attributes(config_manager: ConfigurationManager):
    assert hasattr(config_manager, "load")
    assert hasattr(config_manager, "save")
    assert hasattr(config_manager, "backup")
    assert hasattr(config_manager, "get_value")
    assert hasattr(config_manager, "set_value")
    assert hasattr(config_manager, "evaluate_path")
    assert hasattr(config_manager, "get_environment")
    assert hasattr(config_manager, "get_logger")


def test_mapping(config_manager: ConfigurationManager):
    assert hasattr(config_manager, "_map_template")
    assert isinstance(config_manager._map_template, JSONMapTemplate)
    assert isinstance(config_manager._map_template.data, dict)


def test_get_value(config_manager: ConfigurationManager):
    # Check if a valid key exists
    assert config_manager.get_value("app.provider") == "jsonpycraft"

    # Check for a non-existent key with a default value
    assert config_manager.get_value("app.non_existent_key", "default") == "default"

    # Check if a dict is returned for a valid key
    assert isinstance(config_manager.get_value("app.logs.general"), dict)

    # Check for a non-existent key without a default value
    assert config_manager.get_value("app.non_existent_key") is None


def test_set_value(config_manager: ConfigurationManager):
    # Set a new value for a key
    assert config_manager.set_value("app.new_key", "new_value") is True

    # Verify that the new value was set successfully
    assert config_manager.get_value("app.new_key") == "new_value"

    # Attempt to set a value for an existing key
    assert config_manager.set_value("app.provider", "updated_provider") is True

    # Verify that the existing key's value was updated
    assert config_manager.get_value("app.provider") == "updated_provider"


def test_evaluate_path(config_manager: ConfigurationManager, monkeypatch):
    # Simulate the HOME environment variable
    monkeypatch.setenv("HOME", "/home/testuser")

    print("config data:", config_manager._map_template.data)

    # Verify that the default path is utilized if the given path does not exist.
    assert config_manager.evaluate_path("app.test", "tests/tmp") == "tests/tmp"

    # Verify that the given path exists and is utilized.
    assert config_manager.evaluate_path("app.local", "tests/tmp") == "tests/local"


def test_get_environment(config_manager: ConfigurationManager):
    ...  # TODO


def test_get_logger(config_manager: ConfigurationManager):
    ...  # TODO
