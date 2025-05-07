import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlProps(self):
        node = HTMLNode("a", "some links", None, {"href":"htptp.awsd", "target":"_toNothing"})
        node2 = HTMLNode("p", "paraagraphing", [], None)
        node3 = HTMLNode(None, "random", [], {"rand":"randtext"})
        self.assertEqual(node.props_to_html(), " href='htptp.awsd' target='_toNothing'")
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), " rand='randtext'")

    def test_leafToHtml(self):
        node = LeafNode("a", "some links", {"href":"htptp.awsd", "target":"_toNothing"})
        node2 = LeafNode(None, "paraagraphing")
        self.assertEqual(node.to_html(), "<a href='htptp.awsd' target='_toNothing'>some links</a>")
        self.assertEqual(node2.to_html(), "paraagraphing")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_link_node = LeafNode("a", "checkout", {"href":"www.link"})
        child_node = ParentNode("span", [grandchild_node, grandchild_link_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><a href='www.link'>checkout</a></span></div>",
        )


if __name__ == "__main__":
    unittest.main()