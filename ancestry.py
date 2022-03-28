
from bs4 import BeautifulSoup
import requestssoup = BeautifulSoup(html_doc, 'html.parser')
html_doc ="""html source code here(only tag body copy from inspect "inner html")"""
for tag in soup.div.find_all_next('add tag namefor search here'):
    print (tag)
