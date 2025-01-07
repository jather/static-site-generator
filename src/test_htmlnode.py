import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_parent_node(self):
        test1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(test1.to_html(), expected)

    def test_parent_node3(self):
        test1 = ParentNode("p", [ParentNode("b", [LeafNode("i", "inneritalic")])])
        expected = "<p><b><i>inneritalic</i></b></p>"
        self.assertEqual(test1.to_html(), expected)

    def test_parent_node4(self):
        with self.assertRaises(ValueError):
            test1 = ParentNode("p", None)
            print(test1.to_html())


if __name__ == "__main__":
    unittest.main()
