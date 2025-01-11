import re


def import_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    results = []
    for match in matches:
        results.append(match)
    return results


def import_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    results = []
    for match in matches:
        results.append(match)
    return results
