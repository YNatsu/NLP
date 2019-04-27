# -*- encoding: utf-8 -*- 
# @Contact :  ynatsu233@outlook.com
# @Time    :  4/27/2019 07:28 PM  
# @Author  :  Natsu Yuki

import re

# .  : 除 \n 字符
# \d : 数字字符
# \D : 除数字之外字符
# \s : 空字符
# \S : 非空字符
# \w : 数字、字母、下划线
# \W : 非 数字、字母、下划线
# {} : 指定个数
# *  : 0 或 n 次
# ?  : 1 或 1 次
# +  : 1 或 n 次
# () : 整体
# [] : 字符集
# ^  : 开头
# $  : 结尾
# |  : 或

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())