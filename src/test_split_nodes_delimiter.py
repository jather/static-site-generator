import unittest
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnode
from textnode import TextType
from textnode import TextNode


class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected)

    def test_split_nodes_delimiter2(self):
        node1 = TextNode("This is text with a **bold** word", TextType.NORMAL)
        node2 = TextNode("This is italic text node", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            TextNode("This is italic text node", TextType.ITALIC),
        ]
        self.assertEqual(
            split_nodes_delimiter([node1, node2], "**", TextType.BOLD), expected
        )

    def test_invalid_syntax(self):
        with self.assertRaises(Exception):
            a = split_nodes_delimiter(
                TextNode("Testing code * testing", TextType.NORMAL),
                "*",
                TextType.ITALIC,
            )

    def test_text_to_text_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
    TextNode("This is ", TextType.NORMAL),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.NORMAL),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.NORMAL),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.NORMAL),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.NORMAL),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
        self.assertEqual(text_to_textnode(text), expected)
