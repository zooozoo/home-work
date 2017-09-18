from bs4 import BeautifulSoup

f = open('sample.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'lxml')
# print(soup.a.string)

for num, link in enumerate(soup.find_all('a')):
    print(link.get_text())
