import unittest
from textnode import TextNode, TextType
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type
)

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blockType(self):
        blocksNresults = [
            ("# Big heading", BlockType.HEADING),
            ("### smaller heading", BlockType.HEADING),
            ("```\nsome codes\n```", BlockType.CODE),
            ("1. facts\n2. Facts\n3. Ffacts\n4. long stuff but facts", BlockType.OLIST),
            ("- toDo\n- toDodo\n- toDOdodo", BlockType.ULIST),
            (">I've said something", BlockType.QUOTE),
            ("- I'm good\nIm not\n- I'm good again", BlockType.PARAGRAPH),
            ("##What's wrong?", BlockType.PARAGRAPH)
        ]
        for bR in blocksNresults:
            block_type = block_to_block_type(bR[0])
            self.assertEqual(block_type, bR[1])