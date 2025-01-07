import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_default(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_textnode_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://hxy")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://hxy")
        self.assertEqual(node, node2)

    def test_text_text_node_to_html_node(self):
        textnode = TextNode("This is a text node", TextType.ITALIC)
        expected = "<i>This is a text node</i>"
        self.assertEqual(text_node_to_html_node(textnode).to_html(), expected)

    def test_text_text_node_to_html_node2(self):
        textnode = TextNode("This is a text node", TextType.NORMAL)
        expected = "This is a text node"
        self.assertEqual(text_node_to_html_node(textnode).to_html(), expected)

    def test_text_text_node_to_html_node3(self):
        textnode = TextNode("alttext", TextType.IMAGE, "http://yeah")
        expected = '<img src="http://yeah" alt="alttext">'
        self.assertEqual(text_node_to_html_node(textnode).to_html(), expected)

    def text_text_node_to_html_node_exception(self):
        with self.assertRaises(Exception):
            TextNode("example", TextType.HUH)


if __name__ == "__main__":
    unittest.main()
