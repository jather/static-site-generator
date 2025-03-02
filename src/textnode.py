from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"


def text_node_to_html_node(textnode):
    tag = None
    value = textnode.text
    props = None
    match textnode.text_type:
        case TextType.NORMAL:
            pass
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
            props = {"href": textnode.url}
        case TextType.IMAGE:
            tag = "img"
            props = {"src": textnode.url, "alt": textnode.text}
        case _:
            raise Exception("not a valid text type")
    return LeafNode(tag, value, props)
