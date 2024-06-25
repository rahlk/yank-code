import pytest
from enum import Enum


class MarkdownSamples(Enum):
    MARKDOWN_WITH_INLINE_CODE = "\n# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n+ `def test(): return True`\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n"

    MARKDOWN_WITH_INVALID_CODE_BLOCK = "# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n`\ndef test():\n    return True\n    \ndef test2():\n    return False\n    \nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"

    MARKDOWN_WITH_SINGLE_NAMED_CODE_BLOCK = "# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n```python\ndef test():\n\treturn True\ndef test2():\n\treturn False\n```\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    MARKDOWN_WITH_SINGLE_UNNAMED_CODE_BLOCK = "# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n```\ndef test():\n\treturn True\n\t\ndef test2():\n\treturn False\n```\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    MARKDOWN_WITH_MULTIPLE_NAMED_CODE_BLOCKS = "# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n```python\ndef test():\n    return True\n    \ndef test2():\n    return False\n```\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n```golang\nfunc test() bool {\n    return true\n}\n```\n"

    MARKDOWN_WITH_MULTIPLE_UNNAMED_CODE_BLOCKS = "# Title\nipsum lorem dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n```\ndef test():\n    return True\n    \ndef test2():\n    return False\n```\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n```\nfunc test() bool {\n    return true\n}\n```\n"


# You can also create individual fixtures for each sample if needed
@pytest.fixture
def markdown_with_single_named_code_block():
    return MarkdownSamples.MARKDOWN_WITH_SINGLE_NAMED_CODE_BLOCK.value


@pytest.fixture
def markdown_with_single_unnamed_code_block():
    return MarkdownSamples.MARKDOWN_WITH_SINGLE_UNNAMED_CODE_BLOCK.value


@pytest.fixture
def markdown_with_multiple_named_code_blocks():
    return MarkdownSamples.MARKDOWN_WITH_MULTIPLE_NAMED_CODE_BLOCKS.value


@pytest.fixture
def markdown_with_multiple_unnamed_code_blocks():
    return MarkdownSamples.MARKDOWN_WITH_MULTIPLE_UNNAMED_CODE_BLOCKS.value


@pytest.fixture
def markdown_with_invalid_code_block():
    return MarkdownSamples.MARKDOWN_WITH_INVALID_CODE_BLOCK.value


@pytest.fixture
def markdown_with_inline_code():
    return MarkdownSamples.MARKDOWN_WITH_INLINE_CODE.value
