import unittest
from markdown_to_blocks import markdown_to_blocks 

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_markdown(self):
        markdown_text = "# Heading\n\nThis is a paragraph."
        expected_output = [
                "# Heading", "This is a paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

    def test_empty_markdown(self):
        markdown_text = ""
        expected_output = []
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

    def test_complex_markdown(self):
        markdown_text = "# Heading\n\nThis is a paragraph.\n\n## Subheading\n\nAnother paragraph."
        expected_output = [
        "# Heading", "This is a paragraph.", "## Subheading", "Another paragraph."]