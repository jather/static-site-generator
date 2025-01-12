import shutil
import os
from extract_title import extract_title
from markdown_to_html import markdown_to_html


def generate_page(from_path, template_path, dest_path):
    markdown = ""
    template = ""
    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown = markdown_file.read()
    with open(template_path, "r", encoding="utf-8") as template_file:
        template = template_file.read()
    title = extract_title(markdown)
    html = markdown_to_html(markdown).to_html()
    title_replace = template.replace("{{ Title }}", title)
    html_final = title_replace.replace("{{ Content }}", html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as html_file:
        html_file.write(html_final)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.listdir(dir_path_content) is None:
        return
    for filenode in os.listdir(dir_path_content):
        dir_path_content_child = os.path.join(dir_path_content, filenode)
        if os.path.isfile(dir_path_content_child):
            dest_dir_path_child = os.path.join(
                dest_dir_path, os.path.splitext(filenode)[0] + ".html"
            )
            generate_page(dir_path_content_child, template_path, dest_dir_path_child)
        else:
            dest_dir_path_child = os.path.join(dest_dir_path, filenode)
            generate_pages_recursive(
                dir_path_content_child, template_path, dest_dir_path_child
            )
    return
