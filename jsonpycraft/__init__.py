"""
jsonpycraft/__init__.py

JSONPyCraft: A specialized Python toolkit designed for efficient and structured JSON management.
Copyright (C) 2023 Austin Berrio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from jsonpycraft.core.errors import (
    JSONDecodeErrorHandler,
    JSONEncodeErrorHandler,
    JSONFileErrorHandler,
)
from jsonpycraft.core.singleton import Singleton
from jsonpycraft.core.types import (  # JSONError == EncodeError + DecodeError
    DecodeError,
    EncodeError,
    FileError,
    JSONData,
    JSONError,
    JSONList,
    JSONMap,
)
from jsonpycraft.json.base import JSONBaseTemplate
from jsonpycraft.json.io import dump_json, force_read_json, read_json, write_json
from jsonpycraft.json.list import JSONListTemplate
from jsonpycraft.json.map import JSONMapTemplate
from jsonpycraft.manager.configuration import ConfigurationManager

# Additional project details extracted from pyproject.toml
__version__ = "0.1.3"
__author__ = "Austin Berrio <aberrio@teleprint.me>"
__description__ = "JsonPyCraft is a specialized Python toolkit designed for efficient and structured JSON management."
__license__ = "AGPL-3.0-or-later"
