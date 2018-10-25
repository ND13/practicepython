import bs4 as bs
import urllib.request

url = urllib.request.urlopen("https://www.nytimes.com").read()
soup = bs.BeautifulSoup(url, 'lxml')

for header in soup.find_all(class_='story-heading'):
        print(header.text)


        
