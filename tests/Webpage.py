

from WebManager.Webpage import WebpageManager


test_html1 = """
<h1>Test page 1<h1>
<a href='/test/test/test2'>test</a>
"""

test_html2 = """
<h1>Test page 2<h1>
<a href='/'>return</a>
"""


if __name__ == '__main__':
    webpage = WebpageManager(caveat=False)
    webpage.add_page("index", test_html1)
    webpage.add_page("test/test/test2", test_html2)
    webpage.run()
    ...
