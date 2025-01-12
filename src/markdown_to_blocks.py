import re


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n(\n+)", markdown)
    stripped = [x.strip() for x in blocks if x.strip()]
    return stripped


def block_to_block_type(block):
    lines = block.split("\n")
    if len(lines) == 1 and re.match(r"^#{1,6} .+", lines[0]):
        return "heading"

    def line_match(string):
        nonlocal count
        if re.match(r"^```", string):
            return "code"
        if re.match(r"^>", string):
            return "quote"
        if re.match(r"^[*-] ", string):
            return "unordered_list"
        ordered_match = re.match(r"^(\d)\. ", string)
        if ordered_match:
            if int(ordered_match.group(1)) == count + 1:
                count += 1
                return "ordered_list"
        else:
            return "paragraph"

    count = 0
    guess = line_match(lines[0])
    if len(lines) == 1:
        if guess == "code":
            if re.match(r"^```.+```$"):
                return "code"
            return "paragraph"
        return guess
    for i in range(1, len(lines)):
        if guess == "code":
            if i == len(lines) - 1:
                if re.match(r"```$"):
                    return "code"
                return "paragraph"
            continue
        if line_match(lines[i]) == guess:
            continue
        return "paragraph"
    return guess
