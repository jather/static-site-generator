import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_markdown(self):
        markdown_text = "# Heading\n\nThis is a paragraph."
        expected_output = ["# Heading", "This is a paragraph."]
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

    def test_empty_markdown(self):
        markdown_text = ""
        expected_output = []
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

    def test_complex_markdown(self):
        markdown_text = (
            "# Heading\n\nThis is a paragraph.\n\n## Subheading\n\nAnother paragraph."
        )
        expected_output = [
            "# Heading",
            "This is a paragraph.",
            "## Subheading",
            "Another paragraph.",
        ]
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

    def test_block_to_block_type(self):
        block = "### paragraph"
        expected = "heading"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        block = "```this is a code block```"
        expected = "code"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_ordered_list(self):
        block = "1. blahblah\n2. tnrfytun\n3. tryountfry"
        expected = "ordered_list"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        block = "1. blahblah\n3. tnrfytun\n3. atryountfry"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        block = "```this \nis a \ncode block\n```"
        expected = "code"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_quote(self):
        block = ">wftwytf\n>twytnfwyt\n>wtfynfwto\n>wftw"
        expected = "quote"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        block = "* twyoutnw \n- tryuontfr \n* trftr"
        expected = "unordered_list"
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_paragraph(self):
        block = "* twyouanta\nwftyounwytn"
        expected = "paragraph"
        self.assertEqual(block_to_block_type(block), expected)
