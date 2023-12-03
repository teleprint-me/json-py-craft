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

## Installation

To install JsonPyCraft, run the following command in your terminal:

```bash
pip install https://github.com/teleprint-me/json-py-craft.git
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

## Features

- Robust JSON file handling (load, save, backup).
- Advanced JSON structure manipulation (mapping and list templates).
- Nested JSON data management.
- Pythonic, easy-to-use interface with detailed documentation.

### OpenAI GPT Support

Chat with [JSONPyCraft](https://chat.openai.com/g/g-ECxYHAufF-jsonpycraft) if you have a OpenAI Plus subscription.

## License

JsonPyCraft is released under the [GNU Affero General Public License](LICENSE).

## Contributing, Support, and Contact

For support, feature requests, or contributions, feel free to open an issue or pull request.
