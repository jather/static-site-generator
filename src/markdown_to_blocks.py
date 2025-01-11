import re
def markdown_to_blocks(markdown):
    blocks = re.split(r"\n(\n+)", markdown)
    stripped = [x.strip() for x in blocks if x.strip()]
    return stripped