import re
from html import escape

'''
class MarkdownParser:
    def __init__(self):
        self.block_parsers = [
            self.parse_headers,
            self.parse_code_blocks,
            self.parse_blockquotes,
            self.parse_lists,
            self.parse_paragraphs
        ]
        self.inline_parsers = [
            self.parse_bold,
            self.parse_italic,
            self.parse_code,
            self.parse_links,
            self.parse_images
        ]

    def parse(self, text):
        blocks = self.split_blocks(text)
        html = []
        for block in blocks:
            for parser in self.block_parsers:
                result = parser(block)
                if result:
                    html.append(result)
                    break
        return '\n'.join(html)

    def split_blocks(self, text):
        return re.split(r'\n{2,}', text)

    def parse_inline(self, text):
        for parser in self.inline_parsers:
            text = parser(text)
        return text

    # Block parsers
    def parse_headers(self, block):
        match = re.match(r'^(#{1,6})\s(.+)$', block)
        if match:
            level = len(match.group(1))
            content = self.parse_inline(match.group(2))
            return f'<h{level}>{content}</h{level}>'
        return None

    def parse_code_blocks(self, block):
        if block.startswith('```'):
            lines = block.split('\n')
            language = lines[0][3:]
            code = '\n'.join(lines[1:-1])
            return f'<pre><code class="language-{language}">{escape(code)}</code></pre>'
        return None

    def parse_blockquotes(self, block):
        if block.startswith('> '):
            content = '\n'.join(line[2:] for line in block.split('\n'))
            return f'<blockquote>{self.parse(content)}</blockquote>'
        return None

    def parse_lists(self, block):
        if re.match(r'^(-|\d+\.)\s', block):
            items = re.split(r'\n(?=(-|\d+\.)\s)', block)
            list_type = 'ol' if items[0][0].isdigit() else 'ul'
            parsed_items = []
            for item in items:
                # Remove the list marker and any leading/trailing whitespace
                content = re.sub(r'^(-|\d+\.)\s*', '', item).strip()
                parsed_items.append(f'<li>{self.parse_inline(content)}</li>')
            return f'<{list_type}>{" ".join(parsed_items)}</{list_type}>'
        return None

    def parse_paragraphs(self, block):
        return f'<p>{self.parse_inline(block)}</p>'

    # Inline parsers
    def parse_bold(self, text):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    def parse_italic(self, text):
        return re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    def parse_code(self, text):
        return re.sub(r'`(.*?)`', r'<code>\1</code>', text)

    def parse_links(self, text):
        return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    def parse_images(self, text):
        return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)
'''

import re
from html import escape

class MarkdownParser:
    def __init__(self):
        self.block_parsers = [
            ('heading', r'^(#{1,6})\s(.+)$'),
            ('code_block', r'^```(\w*)\n([\s\S]*?)\n```$'),
            ('blockquote', r'^>\s(.+)$'),
            ('unordered_list', r'^(\s*[-*+]\s.+)(\n\s*[-*+]\s.+)*$'),
            ('ordered_list', r'^(\s*\d+\.\s.+)(\n\s*\d+\.\s.+)*$'),
            ('paragraph', r'^(?!<\/?\w+>|\s*\[.*?\]:\s*\S+)(.+)$'),
        ]
        self.inline_parsers = [
            ('bold', r'\*\*(.*?)\*\*'),
            ('italic', r'\*(.*?)\*'),
            ('code', r'`(.*?)`'),
            ('link', r'\[(.*?)\]\((.*?)\)'),
            ('image', r'!\[(.*?)\]\((.*?)\)'),
        ]

    def parse(self, text):
        lines = text.split('\n')
        parsed_lines = []
        i = 0
        while i < len(lines):
            for block_type, pattern in self.block_parsers:
                match = re.match(pattern, lines[i], re.MULTILINE)
                if match:
                    if block_type == 'heading':
                        level, content = match.groups()
                        parsed_lines.append(f'<h{len(level)}>{self.parse_inline(content)}</h{len(level)}>')
                    elif block_type == 'code_block':
                        lang, code = match.groups()
                        parsed_lines.append(f'<pre><code class="language-{lang}">{escape(code)}</code></pre>')
                        i += code.count('\n') + 2  # Skip the entire code block
                    elif block_type == 'blockquote':
                        content = match.group(1)
                        parsed_lines.append(f'<blockquote>{self.parse_inline(content)}</blockquote>')
                    elif block_type in ('unordered_list', 'ordered_list'):
                        list_items = re.findall(r'\s*[-*+\d\.]\s(.+)', match.group())
                        list_type = 'ul' if block_type == 'unordered_list' else 'ol'
                        parsed_items = [f'<li>{self.parse_inline(item)}</li>' for item in list_items]
                        parsed_lines.append(f'<{list_type}>{" ".join(parsed_items)}</{list_type}>')
                        i += len(list_items) - 1  # Skip processed list items
                    elif block_type == 'paragraph':
                        content = match.group(1)
                        parsed_lines.append(f'<p>{self.parse_inline(content)}</p>')
                    break
            i += 1
        return '\n'.join(parsed_lines)

    def parse_inline(self, text):
        for inline_type, pattern in self.inline_parsers:
            if inline_type == 'bold':
                text = re.sub(pattern, r'<strong>\1</strong>', text)
            elif inline_type == 'italic':
                text = re.sub(pattern, r'<em>\1</em>', text)
            elif inline_type == 'code':
                text = re.sub(pattern, r'<code>\1</code>', text)
            elif inline_type == 'link':
                text = re.sub(pattern, r'<a href="\2">\1</a>', text)
            elif inline_type == 'image':
                text = re.sub(pattern, r'<img src="\2" alt="\1">', text)
        return text

# Usage
parser = MarkdownParser()
markdown_text = """
# Welcome to Markdown

This is a paragraph with **bold** and *italic* text.

```python
def hello_world():
    print("Hello, World!")
```

> This is a blockquote

- Item 1
* Item 2

1. Numbered item 1
2. Numbered item 2

Link to google: [Google](https://www.google.com/)

![image](https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png)

[Google]: https://www.google.com/
"""
html_output = parser.parse(markdown_text)
print(html_output)