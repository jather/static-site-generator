import re


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if re.match(r"^# (.+)", line):
            title = re.match(r"^# (.+)", line).group(1)
            return title.strip()
    raise Exception("no match for title")


print(extract_title("rtafat\n# ftoyrunoyrufnt\nryfotunr\nrtf"))
