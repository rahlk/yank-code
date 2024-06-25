# Yank Code

A treesitter based markdown synthesizer to yank code blocks from markdown. It's designed to make it easy to pull out and use code snippets embedded in documentation and LLM generated markdown output.

## Installation

You can install Yank-Code using pip:

```bash
pip install yank-code
```

Alternatively, you can install from source:

```bash
pip install git+https://github.com/rahlk/yank-code.git
```

## Usage

Here's a simple example of how to use Yank-Code:

```python
from yank_code import extract_code_blocks

markdown_content = """
    # Sample Markdown

    Here's a Python code block:

    ```python
    def hello_world():
        print("Hello, World!")
    ```

    And here's a JavaScript code block:


    ```javascript
    console.log("Hello, World!");
    ```
"""

code_blocks = extract_code_blocks(markdown_content)

for language, code in code_blocks:
    print(f"Language: {language}")
    print(code)
    print("---")

```

This will output:

```plaintext
Language: python
def hello_world():
    print("Hello, World!")
---
Language: javascript
console.log("Hello, World!")
---
```

## Features

- Extracts code blocks from Markdown text
- Identifies the programming language of each code block (if specified)
- Supports multiple code blocks in a single Markdown document

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
