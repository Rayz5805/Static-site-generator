from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text_list = node.text.split(delimiter)
        if len(text_list) % 2 == 0:
            raise Exception("invalid Markdown syntax")
        for i in range(len(text_list)):
            if text_list[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_list[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_list[i], text_type))
    return new_nodes
    
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue

        next_section = node.text
        for image in images:
            text_list = next_section.split(f"![{image[0]}]({image[1]})", 1)
            if len(text_list) != 2:
                raise Exception("invalid Markdown syntax")
            if text_list[0] != "":
                new_nodes.append(TextNode(text_list[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            next_section = text_list[1]

        if next_section != "":
            new_nodes.append(TextNode(next_section, TextType.TEXT))
        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue

        next_section = node.text
        for link in links:
            text_list = next_section.split(f"[{link[0]}]({link[1]})", 1)
            if len(text_list) != 2:
                raise Exception("invalid Markdown syntax")
            if text_list[0] != "":
                new_nodes.append(TextNode(text_list[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            next_section = text_list[1]

        if next_section != "":
            new_nodes.append(TextNode(next_section, TextType.TEXT))
        
    return new_nodes

def text_to_textnodes(text): ###
    text_node = [TextNode(text, TextType.TEXT)]
    
    text_node = split_nodes_delimiter(text_node,  "**", TextType.BOLD)
    text_node = split_nodes_delimiter(text_node,  "_", TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node, "`", TextType.CODE)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    
    return text_node