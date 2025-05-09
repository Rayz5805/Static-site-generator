import sys
import os
import shutil
from generate_html import generate_page

def main():
    basepath = sys.argv
    if not basepath:
        basepath = "/"

    #ensure public directory exist and is empty
    if not os.path.exists("public"):
        os.mkdir("public")
    else:
        shutil.rmtree("public")
        os.mkdir("public")
    
    #copy files from static to public not using copytree
    shutil.copy("static/index.css", "public")
    os.mkdir("public/images")
    for img in os.listdir("static/images"):
        img_path = os.path.join("static/images", img)
        shutil.copy(img_path, "public/images")

    if not os.path.exists("content/index.md"):
        raise Exception("missing index.md file in content directory")
    generate_page_fromPath("content", basepath)

def generate_page_fromPath(content_path, basepath) -> None: 
    '''recursively generate html to public directory matching structure of content directory'''
    for index in os.listdir(content_path):
        current_path = os.path.join(content_path, index)
        public_path = current_path.replace(f"content/", "public/").replace(".md", ".html")
        
        if not os.path.exists(public_path) and os.path.isdir(current_path):
            os.mkdir(public_path)
        if os.path.isfile(current_path):
            generate_page(current_path, "template.html", public_path, basepath)
            continue
        generate_page_fromPath(current_path, basepath)

main()