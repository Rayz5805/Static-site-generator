class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented for this class")
    
    def props_to_html(self):
        allProps = ""
        if self.props == None:
            return allProps
        for prop in self.props.items():
            allProps += f" {prop[0]}=\"{prop[1]}\""
        return allProps
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("missing value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        if self.children == None:
            raise ValueError("missing child")
        htmls = ""
        for child in self.children:
            htmls += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{htmls}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        
            