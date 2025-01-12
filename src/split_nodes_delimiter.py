from textnode import TextNode, TextType
from extract_images_links import import_markdown_links, import_markdown_images


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split = old_node.text.split(delimiter)
        if len(split) < 2:
            new_nodes.append(old_node)
            continue
        if not (len(split) % 2):
            raise Exception("invalid syntax")
        for i in range(0, len(split)):
            if split[i]:
                if i % 2:
                    new_nodes.append(TextNode(split[i], text_type))
                else:
                    new_nodes.append(TextNode(split[i], TextType.NORMAL))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    def image_split(text, property_tuple):
        (alt, src) = property_tuple
        return text.split(f"![{alt}]({src})", 1)

    for old_node in old_nodes:
        if old_node.text_type is not TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        property_tuples = import_markdown_images(old_node.text)
        if not property_tuples:
            new_nodes.append(old_node)
            continue
        current_string = old_node.text
        for image_tuple in property_tuples:
            split_strings = image_split(current_string, image_tuple)
            if split_strings[0]:
                new_nodes.append(TextNode(split_strings[0], TextType.NORMAL))
            new_nodes.append(TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]))
            current_string = split_strings[1]
        if current_string:
            new_nodes.append(TextNode(current_string, TextType.NORMAL))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    def link_split(text, property_tuple):
        (link_text, link) = property_tuple
        return text.split(f"[{link_text}]({link})", 1)

    for old_node in old_nodes:
        if old_node.text_type is not TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        property_tuples = import_markdown_links(old_node.text)
        if not property_tuples:
            new_nodes.append(old_node)
            continue
        current_string = old_node.text
        for link_tuple in property_tuples:
            split_strings = link_split(current_string, link_tuple)
            if split_strings[0]:
                new_nodes.append(TextNode(split_strings[0], TextType.NORMAL))
            new_nodes.append(TextNode(link_tuple[0], TextType.LINK, link_tuple[1]))
            current_string = split_strings[1]
        if current_string:
            new_nodes.append(TextNode(current_string, TextType.NORMAL))
    return new_nodes
