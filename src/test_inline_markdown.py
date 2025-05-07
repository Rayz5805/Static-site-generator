import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
) 


class TestTextNode(unittest.TestCase):
    def test_text_deli_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is `EXPLOSION`", TextType.BOLD)
        node3 = TextNode("This is `EXPLOSION`, `maybe...`", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is `EXPLOSION`", TextType.BOLD),
            TextNode("This is ", TextType.TEXT),
            TextNode("EXPLOSION", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("maybe...", TextType.CODE),
        ])

    def test_text_deli_multi(self):
        node = TextNode("This is **EXPLOSION**, _maybe..._", TextType.TEXT)

        splitBold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        splitItalic_nodes = split_nodes_delimiter(splitBold_nodes, "_", TextType.ITALIC)

        self.assertEqual(splitItalic_nodes,[
            TextNode("This is ", TextType.TEXT),
            TextNode("EXPLOSION", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("maybe...", TextType.ITALIC),
        ])

    def test_extractImg(self):
        text = "Here's my photo ![A cat](https://Catto.com)"
        alturl = extract_markdown_images(text)
        self.assertEqual(alturl, [("A cat", "https://Catto.com")])

    def test_extractLink(self):
        text = "Here's my [portfolio](https://proProgram/b12rt3.web)"
        alturl = extract_markdown_links(text)
        self.assertEqual(alturl, [("portfolio", "https://proProgram/b12rt3.web")])

    def test_splitImg(self):
        node = TextNode("Here's my photo ![A cat](https://Catto.com) and ![A Dog](https://Doggo.com)", TextType.TEXT)
        new_node = split_nodes_image([node])
        self.assertEqual(new_node, [
            TextNode("Here's my photo ", TextType.TEXT),
            TextNode("A cat", TextType.IMAGE, "https://Catto.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("A Dog", TextType.IMAGE, "https://Doggo.com")
        ])

    def test_splitLink(self):
        node = TextNode("Here's my [portfolio](https://proProgram/b12rt3.web) [schedule](https://proProgram.sch/b12rt3.web)", TextType.TEXT)
        new_node = split_nodes_link([node])
        self.assertEqual(new_node, [
            TextNode("Here's my ", TextType.TEXT),
            TextNode("portfolio", TextType.LINK, "https://proProgram/b12rt3.web"),
            TextNode(" ", TextType.TEXT),
            TextNode("schedule", TextType.LINK, "https://proProgram.sch/b12rt3.web")
        ])

    def test_textToTextNode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(text_nodes,[
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])


if __name__ == "__main__":
    unittest.main()