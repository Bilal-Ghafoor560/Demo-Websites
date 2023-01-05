import cssutils
import requests
from bs4  import BeautifulSoup
import os

url='https://discover.teachable.com/search?query=Food'

r=requests.get(url)
soup=BeautifulSoup(r.text, 'html.parser')




html = """<div class="small-card-head"/>"""
soup = BeautifulSoup(html)
div_style = soup.find('div')['style']
style = cssutils.parseStyle(div_style)
url = style['background-image']
url = url.replace('url(', '').replace(')', '')

id = 0
images = soup.find_all('img')
for image in images:
    id = id + 1
    link = image['src']
    with open('file' + str(id) + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)