import os
import shutil

def main():
    if not os.path.exists("../public"):
        os.mkdir("../public")
    shutil.rmtree("../public")
    shutil.copy("../static", "../public")
main()