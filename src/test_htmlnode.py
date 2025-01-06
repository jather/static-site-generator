import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test1 = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test1.props_to_html(), expected)

    def test_props_to_html2(self):
        test1 = HTMLNode(props={"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(test1.props_to_html(), expected)

    def test_leaf_node(self):
        test1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(test1.to_html(), expected)

    def test_leaf_node_2(self):
        test1 = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com", "target": "thisistarget"},
        )
        expected = (
            '<a href="https://www.google.com" target="thisistarget">Click me!</a>'
        )
        self.assertEqual(test1.to_html(), expected)

    def test_leaf_node_3(self):
        test1 = LeafNode("p", "texttesttext")
        expected = "<p>texttesttext</p>"
        self.assertEqual(test1.to_html(), expected)

    def test_leaf_node_4(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()


if __name__ == "__main__":
    unittest.main()
