import sys
import os
import shutil
from generate_html import generate_page

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    generated_dir = "docs"

    #ensure public directory exist and is empty
    if not os.path.exists(generated_dir):
        os.mkdir(generated_dir)
    else:
        shutil.rmtree(generated_dir)
        os.mkdir(generated_dir)
    
    #copy files from static to public not using copytree
    shutil.copy("static/index.css", generated_dir)
    os.mkdir(f"{generated_dir}/images")
    for img in os.listdir("static/images"):
        img_path = os.path.join("static/images", img)
        shutil.copy(img_path, f"{generated_dir}/images")

    if not os.path.exists("content/index.md"):
        raise Exception("missing index.md file in content directory")
    generate_page_fromPath("content", generated_dir, basepath)

def generate_page_fromPath(content_path, generated_dir, basepath) -> None: 
    '''recursively generate html to the generated directory matching structure of content directory'''
    for index in os.listdir(content_path):
        current_path = os.path.join(content_path, index)
        generated_dir_path = current_path.replace(f"content/", f"{generated_dir}/").replace(".md", ".html")
        
        if not os.path.exists(generated_dir_path) and os.path.isdir(current_path):
            os.mkdir(generated_dir_path)
        if os.path.isfile(current_path):
            generate_page(current_path, "template.html", generated_dir_path, basepath)
            continue
        generate_page_fromPath(current_path, generated_dir, basepath)

main()