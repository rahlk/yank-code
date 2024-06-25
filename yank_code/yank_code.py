from typing import List
import tree_sitter_markdown as tsmd
from tree_sitter import Language, Node, Parser


def extract_code_blocks(raw_markdown: str) -> str:
    PY_LANGUAGE = Language(tsmd.language())
    parser = Parser(PY_LANGUAGE)
    tree = parser.parse(raw_markdown.encode())
    tree_node_cursor = tree.root_node.walk()
    fenced_code_blocks: List[Node] = []
    # Do a depth-first search of the tree to find all code blocks
    while True:
        if tree_node_cursor.node.type == "fenced_code_block":
            fenced_code_blocks.append(tree_node_cursor.node)

        # Attempt to go to the first child of the current node
        if tree_node_cursor.goto_first_child():
            # If true, then we've successfully moved to the first child, so we continue.
            continue

        # If the above is false, then there are no more children for this node, so we move to the next sibling
        if tree_node_cursor.goto_next_sibling():
            # If true, then there is a sibling, so we continue again.
            continue

        # If both the above are false, then there are no more children or siblings, so we move to the parent.
        while True:
            # If we have no more parents, then we're done since we have reached the root, so we'll return what we have.
            if not tree_node_cursor.goto_parent():
                return list(map(extract_code_from_block, fenced_code_blocks))

            # Otherwise, we do have a parents, we we'll move to the next sibling of the parent
            if tree_node_cursor.goto_next_sibling():
                break  # Break the inner loop to continue with the outer loop


def extract_code_from_block(node: Node):
    language = None
    for child in node.children:
        if child.type == "info_string":
            language = child.text.decode()
        if child.type == "code_fence_content":
            code = child.text.decode()
            return {"code": code, "language": language}
