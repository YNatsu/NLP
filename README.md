#  NLP

## RE

### [语法](<https://www.runoob.com/regexp/regexp-syntax.html>)

#### 非打印字符

| 字符 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| \cx  | 匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。 |
| \f   | 匹配一个换页符。等价于 \x0c 和 \cL。                         |
| \n   | 匹配一个换行符。等价于 \x0a 和 \cJ。                         |
| \r   | 匹配一个回车符。等价于 \x0d 和 \cM。                         |
| \s   | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符。 |
| \S   | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。                  |
| \t   | 匹配一个制表符。等价于 \x09 和 \cI。                         |
| \v   | 匹配一个垂直制表符。等价于 \x0b 和 \cK。                     |

#### 特殊字符

| 特别字符 | 描述                                                         |
| :------- | :----------------------------------------------------------- |
| $        | 匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。 |
| ( )      | 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。 |
| *        | 匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。     |
| +        | 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。     |
| .        | 匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。    |
| [        | 标记一个中括号表达式的开始。要匹配 [，请使用 \[。            |
| ?        | 匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。 |
| \        | 将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。 |
| ^        | 匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。 |
| {        | 标记限定符表达式的开始。要匹配 {，请使用 \{。                |
| \|       | 指明两项之间的一个选择。要匹配 \|，请使用 \|。               |

#### 限定符

| 字符  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| *     | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
| +     | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
| ?     | 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 、 "does" 中的 "does" 、 "doxy" 中的 "do" 。? 等价于 {0,1}。 |
| {n}   | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
| {n,}  | n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。 |
| {n,m} | m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。 |

#### 定位符

| 字符 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| ^    | 匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。 |
| $    | 匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。 |
| \b   | 匹配一个单词边界，即字与空格间的位置。                       |
| \B   | 非单词边界匹配。                                             |

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

摘自：<https://blog.csdn.net/m0_37952030/article/details/78304088>

### 分词与词性标注

核心函数：nlp.tag(contents, space_mode=0, oov_level=3, t2s=0, special_char_conv=0)

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

核心函数：nlp.sentiment(data, model = 'general')

```python
s = ['他是个傻逼', '美好的世界']

result = nlp.sentiment(s)

print(result)

# [[0.6519134382562579, 0.34808656174374203], [0.92706110187413, 0.07293889812586994]]
# 第一个值为非负面概率，第二个值为负面概率，两个值相加和为 1
```

| 模型名  | 行业 | URL                                                  |
| ------- | ---- | ---------------------------------------------------- |
| general | 通用 | <http://api.bosonnlp.com/sentiment/analysis>         |
| auto    | 汽车 | <http://api.bosonnlp.com/sentiment/analysis?auto>    |
| kitchen | 厨具 | <http://api.bosonnlp.com/sentiment/analysis?kitchen> |
| food    | 餐饮 | <http://api.bosonnlp.com/sentiment/analysis?food>    |
| news    | 新闻 | <http://api.bosonnlp.com/sentiment/analysis?news>    |
| weibo   | 微博 | <http://api.bosonnlp.com/sentiment/analysis?weibo>   |

### 语义联想

核心函数：nlp.suggest(data)

```python
term = '粉丝'
result = nlp.suggest(term, top_k=10)
for score, word in result:
    print(score, word)

# 0.9999999999999994 粉丝/n
# 0.4860246796131101 脑残粉/n
# 0.4763802597640094 听众/n
# 0.457471160374369 球迷/n
# 0.44279396622121603 观众/n
# 0.43996388413040877 喷子/n
# 0.43706751168681585 乐迷/n
# 0.4365171009654034 鳗鱼/n
# 0.43573534612109743 水军/n
# 0.4332090811336725 好友/n
```

### 关键词提取

核心函数：nlp.extract_keywords(text, top_k=None, segmented=False)

```python
keywords = nlp.extract_keywords('病毒式媒体网站：让新闻迅速蔓延', top_k=2)

print(keywords) 

# [[0.5686631749811326, '蔓延'], [0.5671956747680966, '病毒']]

# 返回权重和关键词，所有关键词的权重的平方和为 1
```

### 新闻分类

核心函数：nlp.classify(data)

```python
s = ['俄否决安理会谴责叙军战机空袭阿勒颇平民',
     '邓紫棋谈男友林宥嘉：我觉得我比他唱得好',
     'Facebook收购印度初创公司']

result = nlp.classify(s)

print(result)

# [5, 4, 8]
```

| 编号 | 分类 | 编号 | 分类   |
| ---- | ---- | ---- | ------ |
| 0    | 体育 | 7    | 科技   |
| 1    | 教育 | 8    | 互联网 |
| 2    | 财经 | 9    | 房产   |
| 3    | 社会 | 10   | 国际   |
| 4    | 娱乐 | 11   | 女人   |
| 5    | 军事 | 12   | 汽车   |
| 6    | 国内 | 13   | 游戏   |

### 新闻摘要

核心函数：summary(title, content, word_limit=0.3, not_exceed=False)

```python
content = (
    '腾讯科技讯（刘亚澜）10月22日消息，前优酷土豆技术副总裁'
    '黄冬已于日前正式加盟芒果TV，出任CTO一职。'
    '资料显示，黄冬历任土豆网技术副总裁、优酷土豆集团产品'
    '技术副总裁等职务，曾主持设计、运营过优酷土豆多个'
    '大型高容量产品和系统。'
    '此番加入芒果TV或与芒果TV计划自主研发智能硬件OS有关。'
)

title = '前优酷土豆技术副总裁黄冬加盟芒果TV任CTO'

print(nlp.summary(title, content, 0.1))

# 腾讯科技讯（刘亚澜）10月22日消息，前优酷土豆技术副总裁黄冬已于日前正式加盟芒果TV，出任CTO一职。
```

### 时间转换

**核心函数：nlp.convert_time(data, basetime=None)**

```python
import datetime

r = nlp.convert_time(
    "2013年二月二十八日下午四点三十分二十九秒",
    datetime.datetime.today())

print(r)

# {'timestamp': '2013-02-28 16:30:29', 'type': 'timestamp'}
```

```python
import datetime

print(nlp.convert_time("今天晚上8点到明天下午3点", datetime.datetime(2015, 9, 1)))

# {'timespan': ['2015-09-01 20:00:00', '2015-09-02 15:00:00'], 'type': 'timespan_0'}
```

### 依存文法分析

| 名称 | 解释                              | 举例                                                         |
| ---- | --------------------------------- | ------------------------------------------------------------ |
| ROOT | 核心词                            | 警察*打击*犯罪。                                             |
| SBJ  | 主语成分                          | [*](http://docs.bosonnlp.com/depparser.html#id2)警察*打击犯罪。 |
| OBJ  | 宾语成分                          | 警察打击*犯罪*。                                             |
| PU   | 标点符号                          | 你好*!*                                                      |
| TMP  | 时间成分                          | [*](http://docs.bosonnlp.com/depparser.html#id4)昨天下午*下雨了。 |
| LOC  | 位置成分                          | 我*在北京*开会。                                             |
| MNR  | 方式成分                          | 我*以最快的速度*冲向了终点。                                 |
| POBJ | 介宾成分                          | 他*对客人*很热情。                                           |
| PMOD | 介词修饰                          | 这个产品*直*到今天才完成。                                   |
| NMOD | 名词修饰                          | 这是一个*大*错误。                                           |
| VMOD | 动词修饰                          | 我*狠狠地*打*了*他。                                         |
| VRD  | 动结式 （第二动词为第一动词结果） | 福建省*涌现出*大批人才。                                     |
| DEG  | 连接词“的”结构                    | [*](http://docs.bosonnlp.com/depparser.html#id6)我*的妈妈是超人。 |
| DEV  | “地”结构                          | 他*狠狠*地看我一眼。                                         |
| LC   | 位置词结构                        | 我在*书房*里吃饭。                                           |
| M    | 量词结构                          | 我有*一*只小猪。                                             |
| AMOD | 副词修饰                          | 一批*大*中企业折戟上海。                                     |
| PRN  | 括号成分                          | 北京（*首都*）很大。                                         |
| VC   | 动词“是”修饰                      | 我把你*看做*是妹妹。                                         |
| COOR | 并列关系                          | 希望能*贯彻* [*](http://docs.bosonnlp.com/depparser.html#id8)执行*该方针 |
| CS   | 从属连词成分                      | 如果*可行*，我们进行推广。                                   |
| DEC  | 关系从句“的”                      | 这是*以前不曾遇到过*的情况。                                 |

```python
s = ['我以最快的速度吃了午饭']

result = nlp.depparser(s)

print(' '.join(result[0]['word']))
print(' '.join(result[0]['tag']))
print(result[0]['head'])
print(' '.join(result[0]['role']))

#我 以 最 快 的 速度 吃 了 午饭
# PN P AD VA DEC NN VV AS NN
# [6, 6, 3, 4, 5, 1, -1, 6, 6]
# SBJ MNR VMOD DEC NMOD POBJ ROOT VMOD OBJ
```

### 命名实体识别

| 时间   | time         |
| ------ | ------------ |
| 地点   | location     |
| 人名   | person_name  |
| 组织名 | org_name     |
| 公司名 | company_name |
| 产品名 | product_name |
| 职位   | job_title    |

```python
s = ['对于该小孩是不是郑尚金的孩子，目前已做亲子鉴定，结果还没出来，'
     '纪检部门仍在调查之中。成都商报记者 姚永忠']
result = nlp.ner(s)[0]
words = result['word']
entities = result['entity']

for entity in entities:
    print(''.join(words[entity[0]:entity[1]]), entity[2])

# 郑尚金 person_name
# 成都商报 product_name
# 记者 job_title
# 姚永忠 person_name
```

### 文本聚类引擎

http://docs.bosonnlp.com/cluster.html

### **典型意见**

**http://docs.bosonnlp.com/comments.html**

## pynlpir

GITHUB:<https://github.com/NLPIR-team/NLPIR>

