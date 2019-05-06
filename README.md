#  NLP

## RE

### [语法](<https://www.runoob.com/regexp/regexp-syntax.html>)

#### 非打印字符

![](img//1.png)

#### 特殊字符

![](img//2.png)

#### 限定符

![](img//3.png)

#### 定位符

![](img//4.png)

### re.match

> re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

#### 常规匹配

```python
`import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)

print(result)
print(result.group())
print(result.span())

# <_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
# Hello 123 4567 World_This is a Regex Demo
# (0, 41)
```

#### 泛匹配

```python
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)

print(result)
print(result.group())
print(result.span)

# <_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
# Hello 123 4567 World_This is a Regex Demo
# (0, 41)
```

#### 目标匹配

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)

print(result)
print(result.group(1))
print(result.span())

# <_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567
# (0, 40)
```

#### 贪婪匹配

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)


print(result.group(1))

# 7
```

#### 非贪婪匹配

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)

print(result.group(1))

# 1234567
```

#### 匹配模式

```python
import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

result = re.match('^He.*?(\d+).*?Demo$', content, re.S)

print(result.group(1))

# 1234567
```

### re.search

> re.search 扫描整个字符串并返回第一个成功的匹配。

```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)

print(result.group(1))

# 1234567
```



> 总结：为匹配方便，能用search就不用match

```python
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)

if result:
    print(result.group(1), result.group(2))

# 齐秦 往事随风
```

```python

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)

if result:
    print(result.group(1), result.group(2))
    
# 任贤齐 沧海一声笑
```

```python
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result:
    print(result.group(1), result.group(2))
    
# beyond 光辉岁月
```

### re.findall

> 搜索字符串，以列表形式返回全部能匹配的子串。

```python
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)

print(type(results))

for result in results:
    print(result)
    print(result[0], result[1], result[2])
    
# <class 'list'>
# ('/2.mp3', '任贤齐', '沧海一声笑')
# /2.mp3 任贤齐 沧海一声笑
# ('/3.mp3', '齐秦', '往事随风')
# /3.mp3 齐秦 往事随风
# ('/4.mp3', 'beyond', '光辉岁月')
# /4.mp3 beyond 光辉岁月
# ('/5.mp3', '陈慧琳', '记事本')
# /5.mp3 陈慧琳 记事本
# ('/6.mp3', '邓丽君', '但愿人长久')
# /6.mp3 邓丽君 但愿人长久
```

```python
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)

for result in results:
    print(result[1])

# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久
```

### re.sub

> 替换字符串中每一个匹配的子串后返回替换后的字符串。

```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('\d+', '', content)

print(content)

# Extra stings Hello  World_This is a Regex Demo Extra stings
```

```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('\d+', 'Replacement', content)

print(content)

# Extra stings Hello Replacement World_This is a Regex Demo Extra stings
```

```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('(\d+)', r'\1 8910', content)

print(content)

# Extra stings Hello 1234567 8910 World_This is a Regex Demo Extra stings
```

```python
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
html = re.sub('<a.*?>|</a>', '', html)

print(html)

results = re.findall('<li.*?>(.*?)</li>', html, re.S)

for result in results:
    print(result.strip())
    
# <div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             沧海一声笑
#         </li>
#         <li data-view="4" class="active">
#             往事随风
#         </li>
#         <li data-view="6">光辉岁月</li>
#         <li data-view="5">记事本</li>
#         <li data-view="5">
#             但愿人长久
#         </li>
#     </ul>
# </div>
# 
# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久
```

### re.compile

> 将正则字符串编译成正则表达式对象

```python
import re

content = '''Hello 1234567 World_This
is a Regex Demo'''

pattern = re.compile('Hello.*Demo', re.S)

print(pattern.match(content))

# <_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This\nis a Regex Demo'>
```

```python
import re

p = re.compile(r'\d+')

print(p.split('one1two2three'))

# ['one', 'two', 'three']
```

```python
import re

p = re.compile(r'\d+')

print(p.findall('one1two2three'))

# ['1', '2']
```

```python
import re

p = re.compile(r'(\w+) (\w+)')
s = 'hello world'
print(p.sub(r'\2 \1',s))

# world hello
```

```python
import re

p = re.compile(r'(\w+) (\w+)')
s = 'hello world'
print(p.subn(r'\2 \1', s))
```

## Jieba

> ​	和拉丁语系不同，亚洲语言是不用空格分开每个有意义的词的。而当我们进行自然语言处理的时候，大部分情况下，词汇是我们对句子和文章理解的基础，因此需要一个工具去把完整的文本中分解成粒度更细的词。
>
> ​	jieba就是这样一个非常好用的中文工具，是以分词起家的，但是功能比分词要强大很多。

### 基本分词函数与用法

#### jieba.cut 以及 jieba.cut_for_search 

jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)

**jieba.cut** 方法接受三个输入参数:

- 需要分词的字符串
- cut_all 参数用来控制是否采用全模式
- HMM 参数用来控制是否使用 HMM 模型

**jieba.cut_for_search** 方法接受两个参数

- 需要分词的字符串
- 是否使用 HMM 模型。

该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细

```python
import jieba

seg_list = jieba.cut("我在学习自然语言处理", cut_all=True)

print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

# Full Mode: 我/ 在/ 学习/ 自然/ 自然语言/ 语言/ 处理
# Default Mode: 我/ 在/ 学习/ 自然语言/ 处理
# 他, 毕业, 于, 上海交通大学, ，, 在, 百度, 深度, 学习, 研究院, 进行, 研究
# 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 哈佛, 大学, 哈佛大学, 深造
```

#### jieba.lcut**以及**jieba.lcut_for_search

**jieba.lcut**以及**jieba.lcut_for_search**直接返回 list

```python
import jieba

result_lcut = jieba.lcut("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")

print("/".join(result_lcut))

print("/".join(jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")))

# 小明/硕士/毕业/于/中国科学院/计算所/，/后/在/哈佛大学/深造

# 小明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，/后/在/哈佛/大学/哈佛大学/深造
```

#### 添加用户自定义词典

很多时候我们需要针对自己的场景进行分词，会有一些领域内的专有词汇。

- 1.可以用jieba.load_userdict(file_name)加载用户字典
- 2.少量的词汇可以自己用下面方法手动添加：
  - 用 add_word(word, freq=None, tag=None) 和 del_word(word) 在程序中动态修改词典
  - 用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。

```python
print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))

jieba.suggest_freq(('中', '将'), True)

print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))

# 如果/放到/旧/字典/中将/出错/。
# 如果/放到/旧/字典/中/将/出错/。
```

### 关键词提取

#### 基于 TF-IDF 算法的关键词抽取

import jieba.analyse

- jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
  - sentence 为待提取的文本
  - topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
  - withWeight 为是否一并返回关键词权重值，默认值为 False
  - allowPOS 仅包括指定词性的词，默认值为空，即不筛选

```python
import jieba.analyse as analyse

lines = open('data/NBA.txt', encoding='UTF-8').read()
print ("  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=())))

# 韦少  杜兰特  全明星  全明星赛  MVP  威少  正赛  科尔  投篮  勇士  球员  斯布鲁克  更衣柜  NBA  三连庄  张卫平  西部  指导  雷霆  明星队
```

```python
lines = open(u'data/西游记.txt',mode='rb').read()
print ("  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=())))

# 行者  八戒  师父  三藏  唐僧  大圣  沙僧  妖精  菩萨  和尚  那怪  那里  长老  呆子  徒弟  怎么  不知  老孙  国王  一个
```

#### 关于TF-IDF 算法的关键词抽取补充

- 关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
  - 用法： jieba.analyse.set_idf_path(file_name) # file_name为自定义语料库的路径
    - 自定义语料库示例见[这里](https://github.com/fxsjy/jieba/blob/master/extra_dict/idf.txt.big)
    - 用法示例见[这里](https://github.com/fxsjy/jieba/blob/master/test/extract_tags_idfpath.py)
  - 关键词提取所使用停止词（Stop Words）文本语料库可以切换成自定义语料库的路径
    - 用法： jieba.analyse.set_stop_words(file_name) # file_name为自定义语料库的路径
    - 自定义语料库示例见[这里](https://github.com/fxsjy/jieba/blob/master/extra_dict/stop_words.txt)
    - 用法示例见[这里](https://github.com/fxsjy/jieba/blob/master/test/extract_tags_stop_words.py)
- 关键词一并返回关键词权重值示例
  - 用法示例见[这里](https://github.com/fxsjy/jieba/blob/master/test/extract_tags_with_weight.py)

#### 基于 TextRank 算法的关键词抽取

- jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 直接使用，接口相同，注意默认过滤词性。
- jieba.analyse.TextRank() 新建自定义 TextRank 实例

算法论文： [TextRank: Bringing Order into Texts](http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)

基本思想:

- 将待抽取关键词的文本进行分词
- 以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
- 计算图中节点的PageRank，注意是无向带权图

```python
import jieba.analyse as analyse
lines = open('data/NBA.txt','rb').read()
print ("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))))
print ("---------------------我是分割线----------------")
print ("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n'))))

# 全明星赛  勇士  正赛  指导  对方  投篮  球员  没有  出现  时间  威少  认为  看来  结果  相隔  助攻  现场  三连庄  介绍  嘉宾
# ---------------------我是分割线----------------
# 勇士  正赛  全明星赛  指导  投篮  玩命  时间  对方  现场  结果  球员  嘉宾  时候  全队  主持人  照片  全程  目标  快船队  肥皂剧
```

### 词性标注

- jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
- 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
- 具体的词性对照表参见[计算所汉语词性标记集](http://ictclas.nlpir.org/nlpir/html/readme.htm)

```python
import jieba.posseg as pseg
words = pseg.cut("我爱自然语言处理")
for word, flag in words:
    print('%s %s' % (word, flag))

# 我 r
# 爱 v
# 自然语言 l
# 处理 v
```

### 并行分词

原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升 基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows

用法：

```python
jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
jieba.disable_parallel() # 关闭并行分词模式
```

实验结果：在 4 核 3.4GHz Linux 机器上，对金庸全集进行精确分词，获得了 1MB/s 的速度，是单进程版的 3.3 倍。

注意：并行分词仅支持默认分词器 jieba.dt 和 jieba.posseg.dt。

```python
import sys
import time
import jieba

jieba.enable_parallel()
content = open(u'data/西游记.txt', "rb").read()
t1 = time.time()
words = "/ ".join(jieba.cut(content))
t2 = time.time()
tm_cost = t2 - t1
print('并行分词速度为 %s bytes/second' % (len(content) / tm_cost))

jieba.disable_parallel()
content = open(u'data/西游记.txt', "rb").read()
t1 = time.time()
words = "/ ".join(jieba.cut(content))
t2 = time.time()
tm_cost = t2 - t1
print('非并行分词速度为 %s bytes/second' % (len(content) / tm_cost))

# 并行分词速度为 830619.50933 bytes/second
# 非并行分词速度为 259941.448353 bytes/second
```

### Tokenize：返回词语在原文的起止位置

注意，输入参数只接受 unicode

```python
print("这是默认模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))

print("\n-----------我是神奇的分割线------------\n")

print("这是搜索模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用', mode='search')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))


# 这是默认模式的tokenize
# 
# 自然语言     start: 0      end:4
# 处理       start: 4      end:6
# 非常       start: 6      end:8
# 有用       start: 8      end:10
# 
# -----------我是神奇的分割线------------
# 
# 这是搜索模式的tokenize
# 自然       start: 0      end:2
# 语言       start: 2      end:4
# 自然语言     start: 0      end:4
# 处理       start: 4      end:6
# 非常       start: 6      end:8
# 有用       start: 8      end:10
```

### [ChineseAnalyzer for Whoosh 搜索引擎](<https://www.jianshu.com/p/127c8c0b908a>)

- `from jieba.analyse import ChineseAnalyzer`

```python
from __future__ import unicode_literals
import sys, os
import jieba.analyse as analyse
import jieba

sys.path.append("../")

# pip install whoosh

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

analyzer = jieba.analyse.ChineseAnalyzer()
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))

if not os.path.exists("tmp"):
    os.mkdir("tmp")

ix = create_in("tmp", schema)  # for create new index
# ix = open_dir("tmp") # for read only
writer = ix.writer()

writer.add_document(
    title="document1",
    path="/a",
    content="This is the first document we’ve added!"
)

writer.add_document(
    title="document2",
    path="/b",
    content="The second one 你 中文测试中文 is even more interesting! 吃水果"
)

writer.add_document(
    title="document3",
    path="/c",
    content="买水果然后来世博园。"
)

writer.add_document(
    title="document4",
    path="/c",
    content="工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
)

writer.add_document(
    title="document4",
    path="/c",
    content="咱俩交换一下吧。"
)

writer.commit()
searcher = ix.searcher()
parser = QueryParser("content", schema=ix.schema)

for keyword in ("水果世博园", "你", "first", "中文", "交换机", "交换"):
    print(keyword + "的结果为如下：")
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:
        print(hit.highlights("content"))
    print("\n--------------我是神奇的分割线--------------\n")

for t in analyzer("我的好朋友是李明;我爱北京天安门;IBM和Microsoft; I have a dream. this is intetesting and interested me a lot"):
    print(t.text)


# 水果世博园的结果为如下：
# 买<b class="match term0">水果</b>然后来<b class="match term1">世博园</b>
# 
# --------------我是神奇的分割线--------------
# 
# 你的结果为如下：
# second one <b class="match term0">你</b> 中文测试中文 is even more interesting
# 
# --------------我是神奇的分割线--------------
# 
# first的结果为如下：
# <b class="match term0">first</b> document we’ve added
# 
# --------------我是神奇的分割线--------------
# 
# 中文的结果为如下：
# second one 你 <b class="match term0">中文</b>测试<b class="match term0">中文</b> is even more interesting
# 
# --------------我是神奇的分割线--------------
# 
# 交换机的结果为如下：
# 干事每月经过下属科室都要亲口交代24口<b class="match term0">交换机</b>等技术性器件的安装工作
# 
# --------------我是神奇的分割线--------------
# 
# 交换的结果为如下：
# 咱俩<b class="match term0">交换</b>一下吧
# 干事每月经过下属科室都要亲口交代24口<b class="match term0">交换</b>机等技术性器件的安装工作
# 
# --------------我是神奇的分割线--------------
# 
# 我
# 好
# 朋友
# 是
# 李明
# 我
# 爱
# 北京
# 天安
# 天安门
# ibm
# microsoft
# dream
# intetest
# interest
# me
# lot
```

## bosonnlp

### 中文分词、词性

```python
# https://bosonnlp.com/console
from bosonnlp import BosonNLP

s = ['亚投行意向创始成员国确定为57个', '“流量贵”频被吐槽']

nlp = BosonNLP('jkk69hrE.34263.MwdMVTH2I0Zs')

result = nlp.tag(s)

for d in result:
    print(' '.join(['%s-%s' % it for it in zip(d['word'], d['tag'])]))
    
# 亚投行-n 意向-n 创始-vi 成员国-n 确定-v 为-v 57-m 个-q
# “-wyz 流量-n 贵-a ”-wyy 频-d 被-pbei 吐槽-v

# http://docs.bosonnlp.com/tag_rule.html 词性标注说明
```

### 情感分析

```python
s = ['他是个傻逼', '美好的世界']

result = nlp.sentiment(s)

print(result)

# [[0.6519134382562579, 0.34808656174374203], [0.92706110187413, 0.07293889812586994]]
```