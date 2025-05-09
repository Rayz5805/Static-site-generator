import unittest

from generate_html import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_get_title(self):
        md = """
# I'm title

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        title = extract_title(md)
        self.assertEqual(title, "I'm title")