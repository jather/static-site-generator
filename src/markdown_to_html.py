import re
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode, LeafNode
from split_nodes_delimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


def text_to_textnode(text):
    Full = TextNode(text, TextType.NORMAL)
    processed = split_nodes_link(split_nodes_image([Full]))
    delimiter_types = [
        ("`", TextType.CODE),
        ("**", TextType.BOLD),
        ("*", TextType.ITALIC),
    ]
    for delimiter in delimiter_types:
        processed = split_nodes_delimiter(processed, delimiter[0], delimiter[1])
    return processed


def text_to_html_nodes(text):
    textnodes = text_to_textnode(text)
    html_nodes = [text_node_to_html_node(textnode) for textnode in textnodes]
    return html_nodes


def text_to_code_block(block):
    stripped = block.strip("`")
    inner = ParentNode("code", text_to_html_nodes(stripped))
    return ParentNode("pre", [inner])


def text_to_blockquote(block):
    lines = block.split("\n")
    return ParentNode("block")


def text_to_list(block, type):
    lines = block.split("\n")
    if type == "ol":
        item_nodes = [ParentNode("li", text_to_html_nodes(line[3:])) for line in lines]
    if type == "ul":
        item_nodes = [ParentNode("li", text_to_html_nodes(line[2:])) for line in lines]
    return ParentNode(type, item_nodes)


def text_to_heading_block(block, number):
    return ParentNode(f"h{str(number)}", text_to_html_nodes(block[number + 1 :]))


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        match block_to_block_type(block):
            case "code":
                block_nodes.append(text_to_code_block(block))
            case "heading":
                header_symbol = re.match(r"^(#+) ", block)
                number = len(header_symbol.group(1))
                block_nodes.append(text_to_heading_block(block, number))
            case "ordered_list":
                block_nodes.append(text_to_list(block, "ol"))
            case "unordered_list":
                block_nodes.append(text_to_list(block, "ul"))
            case "quote":
                block_nodes.append(
                    ParentNode(
                        "blockquote",
                        text_to_html_nodes(
                            "\n".join([line[2:] for line in block.split("\n")])
                        ),
                    )
                )
            case "paragraph":
                block_nodes.append(ParentNode("p", text_to_html_nodes(block)))
            case _:
                raise Exception
    return ParentNode("div", block_nodes)


# markdown_sample = """# Markdown Sample\n\nMarkdown is a lightweight markup language for creating formatted text. Here's an example:\n\n## Headings\n\nUse `#` for headings. For example:\n\n- `# Heading 1`\n- `## Heading 2`\n- `### Heading 3`\n\n## Lists\n\n### Unordered List\n- Item 1\n- Item 2\n  - Sub-item 2.1\n  - Sub-item 2.2\n\n### Ordered List\n1. First item\n2. Second item\n3. Third item\n\n## Links and Images\n\n[Link to Google](https://www.google.com)\n\n![Sample Image](https://via.placeholder.com/150 \"Placeholder Image\")\n\n## Text Formatting\n\n- **Bold text**: `**Bold text**`\n- *Italic text*: `*Italic text*`\n- ~~Strikethrough~~: `~~Strikethrough~~`\n\n## Code\n\nInline `code` example: `` `code` ``\n\nBlock of code:\n```python\ndef hello_world():\n    print(\"Hello, World!\")\n```\n\n## Tables\n\n| Header 1 | Header 2 | Header 3 |\n|----------|----------|----------|\n| Row 1    | Data     | More     |\n| Row 2    | Data     | More     |\n\n## Blockquote\n\n> This is a blockquote. It's great for quoting text.\n\n## Horizontal Rule\n\n---\n\nThat's it! Markdown is simple and easy to use."""
# print(markdown_to_html(markdown_sample))
