import unittest
from split_nodes_delimiter import split_nodes_delimiter
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
