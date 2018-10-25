# Exercise 19 from practicepython.org
# Used lxml instead of beautifulsoup to parse the page

import requests
import lxml.html

def main():
    request_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    request = requests.get(request_url)
    tree = lxml.html.fromstring(request.content)
    
    p_content = tree.xpath('//p//text()')

    print(p_content)


if __name__ == '__main__':
    main()
