class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        props_string = ""
        if self.props is None:
            raise ValueError("props cannot be None")
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'
        return props_string

    def __repr__(self):
        return f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.tag is "img":
            return f"<img{self.props_to_html()}>"
        if self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, child, props=None):
        super().__init__(tag, None, child, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("must have a tag value")
        if self.children is None:
            raise ValueError("wtf? where are the children")
        current_html = f"<{self.tag}>"
        for child in self.children:
            current_html += child.to_html()
        return current_html + f"</{self.tag}>"
