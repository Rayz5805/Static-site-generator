from md_to_html_node import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.strip("#").strip()
    raise Exception("missing h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as fp:
        md_content = fp.read()
    with open(template_path, "r") as tmp:
        tmp_content = tmp.read()
    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    html_title = extract_title(md_content)
    html_content = tmp_content.replace("{{ Title }}", html_title).replace("{{ Content }}", html_string)
    rooted_html_content = html_content.replace("href='/", f"href='{basepath}").replace("src='/", f"src='{basepath}")

    with open(dest_path, "w") as dest:
        dest.write(rooted_html_content)
    