from functools import wraps, lru_cache
from typing import List, Callable, Optional


class Element:
    def __init__(self, tag: str, closing_tag: bool = True):
        self.tag = tag
        self.closing_tag = closing_tag

    def __call__(self, **kwargs): 
        attributes = []
        body_content = kwargs.pop('body', '')
        if self.closing_tag and body_content=='':
            raise ValueError(f"`{self.tag}` requires a parameter `body` with content")
        for key, value in kwargs.items():
            key = key.replace('_', '-')
            key = 'class' if key == 'cls' else key
            attributes.append(f'{key}="{value}"')
        attr_str = ' '.join(attributes)
        if not self.closing_tag:
            return f"<{self.tag} {attr_str} />"
        if isinstance(body_content, list):
            body_content = ''.join(str(item) for item in body_content)
        return f"<{self.tag} {attr_str}>{body_content}</{self.tag}>"
            
    def __str__(self):
        return self()

def create_element(tag: str, closing_tag: bool=True):
    element = Element(tag, closing_tag)
    @lru_cache(maxsize=1000)
    def element_factory(**kwargs):
        return element(**kwargs)
    return element_factory


########################
# Structural HTML Tags #
########################
i = create_element("i")
a = create_element("a")
b = create_element("b")
p = create_element("p")
s = create_element("s")
u = create_element("u")
h1 = create_element("h1")
h2 = create_element("h2")
h3 = create_element("h3")
h4 = create_element("h4")
h5 = create_element("h5")
h6 = create_element("h6")
dd = create_element("dd")
dl = create_element("dl")
dt = create_element("dt")
em = create_element("em")
li = create_element("li")
rp = create_element("rp")
rt = create_element("rt")
ol = create_element("ol")
ul = create_element("ul")
td = create_element("td")
th = create_element("th")
tr = create_element("tr")
var = create_element("var")
nav = create_element("nav")
sub = create_element("sub")
sup = create_element("sup")
svg = create_element("svg")
ins = create_element("ins")
kbd = create_element("kbd")
dfn = create_element("dfn")
div = create_element("div")
del_ = create_element("del")
map_ = create_element("map")
ruby = create_element("ruby")
samp = create_element("samp")
slot = create_element("slot")
span = create_element("span")
html = create_element("html")
form = create_element("form")
head = create_element("head")
abbr = create_element("abbr")
main = create_element("main")
mark = create_element("mark")
math = create_element("math")
menu = create_element("menu")
body = create_element("body")
cite = create_element("cite")
code = create_element("code")
data = create_element("data")
time_ = create_element("time")
aside = create_element("aside")
audio = create_element("audio")
style = create_element("style")
table = create_element("table")
tbody = create_element("tbody")
video = create_element("video")
small = create_element("small")
label = create_element("label")
meter = create_element("meter")
tfoot = create_element("tfoot")
thead = create_element("thead")
title = create_element("title")
hgroup = create_element("hroup")
script = create_element("script")
select = create_element("select")
strong = create_element("strong")
legend = create_element("legend")
option = create_element("option")
output = create_element("output")
button = create_element("button")
canvas = create_element("canvas")
dialog = create_element("dialog")
figure = create_element("figure")
footer = create_element("footer")
header = create_element("header")
iframe = create_element("iframe")
object_ = create_element("object")
section = create_element("section")
summary = create_element("summary")
caption = create_element("caption")
address = create_element("address")
article = create_element("article")
details = create_element("details")
fieldset = create_element("fieldset")
colgroup = create_element("colgroup")
datalist = create_element("datalist")
template = create_element("template")
textarea = create_element("textarea")
noscript = create_element("noscript")
optgroup = create_element("optgroup")
figcaption = create_element("figcaption")
blockquote = create_element("blockquote")
hr = create_element("hr", closing_tag=False)
br = create_element("br", closing_tag=False)
img = create_element("img", closing_tag=False)
col = create_element("col", closing_tag=False)
wbr = create_element("wbr", closing_tag=False)
area = create_element("area", closing_tag=False)
base = create_element("base", closing_tag=False)
link = create_element("link", closing_tag=False)
meta = create_element("meta", closing_tag=False)
track = create_element("track", closing_tag=False)
embed = create_element("embed", closing_tag=False)
input_ = create_element("input", closing_tag=False)
source = create_element("source", closing_tag=False)
menuitem = create_element("menuitem", closing_tag=False)


















