# JSONPyCraft

<figure>
    <p align="center">
        <img src="assets/logo.png"
            alt="JsonPyCraft Artwork Image"
            width="256" height="256">
        <figcaption>JsonPyCraft - A Fusion of Python and JSON, symbolizing the toolkit's capability to manage intricate JSON data structures.</figcaption>
    </p>
</figure>

## Description
JsonPyCraft is a specialized Python toolkit designed for efficient and structured JSON management. This toolkit offers a range of functionalities from basic JSON file handling to advanced operations, making it ideal for developers looking to manage JSON data in Python applications with precision and ease.

## Features

- Robust JSON file handling (load, save, backup).
- Advanced JSON structure manipulation (mapping and list templates).
- Nested JSON data management.
- Pythonic, easy-to-use interface with detailed documentation.

## JSONPyCraft Documentation

Welcome to the JSONPyCraft documentation! Explore detailed documentation on key aspects of JSONPyCraft:

- **[Core Components](docs/core/README.md):** Learn about custom error handling, the Singleton pattern, core types, and more.

- **[JSON Templates](docs/json/README.md):** Understand JSON templates, I/O operations, list templates, and map templates.

- **[Managers](docs/manager/README.md):** Discover the `ConfigurationManager` class for managing configuration data.

- **[PlantUML Diagrams](docs/puml/README.md):** Visual representations of key components.

For more detailed information, check out the [full documentation index](docs/README.md).

### OpenAI GPT Support

JsonPyCraft supports integration with OpenAI GPT if you have an OpenAI Plus subscription. You can chat with [JSONPyCraft](https://chat.openai.com/g/g-ECxYHAufF-jsonpycraft) for more information.

## Installation

You can install JsonPyCraft using either `pip` or `poetry`. Follow the instructions below based on your preferred method.

### Using pip:

1. Create a virtual environment (optional but recommended for isolation):

```bash
virtualenv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

3. Install JsonPyCraft using `pip`:

```bash
pip install https://github.com/teleprint-me/json-py-craft.git
```

### Using poetry:

1. Initialize a new Poetry project. If you haven't already installed Poetry, you can do so with `pip`:

```bash
pip install poetry
```

2. Navigate to your project directory and run:

```bash
poetry init
```

Follow the prompts and add any necessary packages to your project.

3. Activate the Poetry shell:

```bash
poetry shell
```

4. Add JsonPyCraft to your project using the following command, specifying the URL to the wheel file:

```bash
poetry add https://github.com/teleprint-me/json-py-craft/releases/download/v0.1.0/jsonpycraft-0.1.0-py3-none-any.whl
```

## Usage

Here's a quick start guide to using JsonPyCraft:

```python
from jsonpycraft import JSONMapTemplate, JSONListTemplate

# Example of using JSONMapTemplate
map_template = JSONMapTemplate('map_data.json')
map_template.create('key', 'value')

# Example of using JSONListTemplate
list_template = JSONListTemplate('list_data.json')
list_template.append({'id': 1, 'name': 'JsonPyCraft'})
```

## Contributing, Support, and Contact

For support, feature requests, or contributions, feel free to open an issue or pull request.

## License

- [LICENSE](LICENSE): JsonPyCraft is released under the GNU Affero General Public License.
