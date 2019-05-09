import requests
from bs4 import BeautifulSoup as bs
import re
from bosonnlp import BosonNLP
from pyecharts import WordCloud


def GetRequests(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = requests.get(url=url, headers=headers)
    return request.content


url = 'https://news.sina.com.cn/c/xl/2019-05-08/doc-ihvhiews0648098.shtml'

request = GetRequests(url)

soup = bs(request, 'lxml')

pattern = re.compile(r'<p>(.*)?</p>')

s = ''

for p in soup.findAll('p'):
    p = str(p)
    m = pattern.match(p)
    if m:
        s += m.group(1).strip()

nlp = BosonNLP('jkk69hrE.34263.MwdMVTH2I0Zs')

result = nlp.tag(s)[0]
dict = {}

print(type(dict))
for word, tag in zip(result['word'], result['tag']):

    if tag[0] == 'n' or tag == 'v' or tag == 'ad':
        print(word, tag)
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1

name = dict.keys()
value = dict.values()

wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])

wordcloud.show_config()
wordcloud.render()






