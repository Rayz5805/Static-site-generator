import unittest
from htmlnode import *
from md_to_html_node import markdown_to_html_node, text_to_children

class TestTextNode(unittest.TestCase):
    def test_markdown_to_htmlnode(self):
        md = """
# Big heading

### small heading

parasyndrom **REDUCTED** can be danger
here is the thingy [web](https://huh.com)

- idk _thing_
- idk `thong`
- idk thang

another paragraph with ![image](/stuff/bee.png), that's the _best_ part

1. be
2. **bee**
3. beee
4. beeee

>My word is good
>because it spelled like that

```
my code
next _line_ of code
```
"""
        html_node = markdown_to_html_node(md)
        html_content = html_node.to_html()
        self.assertEqual(html_content, "<div><h1>Big heading</h1><h3>small heading</h3><p>parasyndrom <b>REDUCTED</b> can be danger here is the thingy <a href='https://huh.com'>web</a></p><ul><li>idk <i>thing</i></li><li>idk <code>thong</code></li><li>idk thang</li></ul><p>another paragraph with <img src='/stuff/bee.png' alt='image'></img>, that's the <i>best</i> part</p><ol><li>be</li><li><b>bee</b></li><li>beee</li><li>beeee</li></ol><blockquote>My word is good because it spelled like that</blockquote><pre><code>my code\nnext _line_ of code\n</code></pre></div>")
