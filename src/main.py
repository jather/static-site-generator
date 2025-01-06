from textnode import TextNode
from textnode import TextType


def main():
    test = TextNode("testing text", TextType.ITALIC, "http://boot.dev")
    print(test)


main()
