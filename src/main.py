from generate_page import generate_pages_recursive
from textnode import TextNode
from textnode import TextType
import os
import shutil


def copy_directory(source_directory, destination_directory):
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
    os.mkdir(destination_directory)

    def recursive_copy(source, destination):
        if os.listdir(source) is None:
            return
        for child in os.listdir(source):
            source_child = os.path.join(source, child)
            destination_child = os.path.join(destination, child)
            if os.path.isfile(source_child):
                shutil.copy(source_child, destination_child)
            else:
                os.mkdir(destination_child)
                recursive_copy(source_child, destination_child)
        return

    recursive_copy(source_directory, destination_directory)


def main():
    copy_directory("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
