from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in blocks:
        block_nodes = block_to_node(block)
        html_children.append(block_nodes)
    html_node = ParentNode("div", html_children)
    return html_node
            
def block_to_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_node(block)
        case BlockType.HEADING:
            return heading_to_node(block)
        case BlockType.CODE:
            return code_to_node(block)
        case BlockType.QUOTE:
            return quote_to_node(block)
        case BlockType.ULIST:
            return ulist_to_node(block)
        case BlockType.OLIST:
            return olist_to_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        children.append(leaf_node)
    return children

def paragraph_to_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_node(block):
    head_count = 0
    while "#" in block:
        block = block[1:]
        head_count += 1
    children = text_to_children(block.strip())
    return ParentNode(f"h{head_count}", children)

def code_to_node(block):
    clean_code = block[4:-3]
    code_parent = LeafNode("code", clean_code)
    return ParentNode("pre", [code_parent])

def quote_to_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_node(block):
    lines = block.split("\n")
    children = []
    for li in lines:
        leaf_nodes = text_to_children(li[2:])
        li_parent = ParentNode("li", leaf_nodes)
        children.append(li_parent)
    return ParentNode("ul", children)

def olist_to_node(block):
    lines = block.split("\n")
    children = []
    for li in lines:
        leaf_nodes = text_to_children(li[3:])
        li_parent = ParentNode("li", leaf_nodes)
        children.append(li_parent)
    return ParentNode("ol", children)