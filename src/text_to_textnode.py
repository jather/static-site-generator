from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnode(text):
    Full = TextNode(text, TextType.NORMAL)
    processed = split_nodes_link(split_nodes_image([Full]))
    delimiter_types = [("`", TextType.CODE), ("**", TextType.BOLD),("*", TextType.ITALIC)]
    for delimiter in delimiter_types:
        processed = split_nodes_delimiter(processed, delimiter[0], delimiter[1])
    return processed