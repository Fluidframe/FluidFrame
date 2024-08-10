import re
from itertools import chain

def extract_classes(html):
    pattern = r'class\s*=\s*["\']([^"\']+)["\']'
    matches = ' '.join(re.findall(pattern, html))
    class_set = set(matches.split())
    return class_set

# Example usage
html_example = '''
<div class="container main-content">
    <p class="text-large bold">Some text</p>
    <span class="highlight text-large">Highlighted text</span>
    <a class="link external" href="#">Link</a>
</div>
'''

extracted_classes = extract_classes(html_example)
print("Extracted classes:", extracted_classes)