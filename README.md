# NLP

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

### Python Code

#### 常规匹配

```python
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)

print(result)
print(result.group())
print(result.span())
```

