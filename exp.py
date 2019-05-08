import pynlpir

title = '仙桃“网红”景点走红的背后 “内功”还需提升'

pynlpir.open()

r = pynlpir.segment(title)

print(r)

pynlpir.close()