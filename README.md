# JsonPyCraft

<figure align="center">
    <img src="assets/logo.png"
         alt="JsonPyCraft Artwork Image"
         width="256" height="256">
    <figcaption>JsonPyCraft - A Fusion of Python and JSON, symbolizing the toolkit's capability to manage intricate JSON data structures.</figcaption>
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
from jsonpycraft import JSONMappingTemplate, JSONListTemplate

# Example of using JSONMapTemplate
mapping = JSONMapTemplate('config.json')
mapping.create('key', 'value')

# Example of using JSONListTemplate
list_template = JSONListTemplate('data.json')
list_template.append({'id': 1, 'name': 'JsonPyCraft'})
```

## Features

- Robust JSON file handling (load, save, backup).
- Advanced JSON structure manipulation (mapping and list templates).
- Nested JSON data management.
- Pythonic, easy-to-use interface with detailed documentation.

## Contributing

Contributions to JsonPyCraft are welcome! Please refer to our contributing guidelines for more information.

## License

JsonPyCraft is released under the [GNU Affero General Public License](LICENSE).

## Support and Contact

For support, feature requests, or contributions, feel free to open an issue or pull request.
