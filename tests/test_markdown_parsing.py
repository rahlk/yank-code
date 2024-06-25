from yank_code.yank_code import extract_code_blocks


def test_extract_code_blocks_single_named(markdown_with_single_named_code_block):
    code_blocks = extract_code_blocks(markdown_with_single_named_code_block)
    assert len(code_blocks) == 1
    assert code_blocks[0]["language"] == "python"
    assert "def test():" in code_blocks[0]["code"]
    assert "def test2():" in code_blocks[0]["code"]


def test_extract_code_blocks_single_unnamed(markdown_with_single_unnamed_code_block):
    code_blocks = extract_code_blocks(markdown_with_single_unnamed_code_block)
    assert len(code_blocks) == 1
    assert code_blocks[0]["language"] is None
    assert "def test():" in code_blocks[0]["code"]
    assert "def test2():" in code_blocks[0]["code"]


def test_extract_code_blocks_multiple_named(markdown_with_multiple_named_code_blocks):
    code_blocks = extract_code_blocks(markdown_with_multiple_named_code_blocks)
    assert len(code_blocks) == 2
    assert code_blocks[0]["language"] == "python"
    assert code_blocks[1]["language"] == "golang"
    assert "def test():" in code_blocks[0]["code"]
    assert "func test() bool {" in code_blocks[1]["code"]


def test_extract_code_blocks_multiple_unnamed(
    markdown_with_multiple_unnamed_code_blocks,
):
    code_blocks = extract_code_blocks(markdown_with_multiple_unnamed_code_blocks)
    assert len(code_blocks) == 2
    assert all(block["language"] is None for block in code_blocks)
    assert "def test():" in code_blocks[0]["code"]
    assert "func test() bool {" in code_blocks[1]["code"]


def test_extract_code_blocks_invalid(markdown_with_invalid_code_block):
    code_blocks = extract_code_blocks(markdown_with_invalid_code_block)
    assert len(code_blocks) == 0


def test_extract_code_blocks_inline(markdown_with_inline_code):
    code_blocks = extract_code_blocks(markdown_with_inline_code)
    assert len(code_blocks) == 0


def test_extract_code_blocks_empty_input():
    code_blocks = extract_code_blocks("")
    assert len(code_blocks) == 0


def test_extract_code_blocks_no_code_blocks():
    markdown = "# Title\nThis is a paragraph without any code blocks."
    code_blocks = extract_code_blocks(markdown)
    assert len(code_blocks) == 0
