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