#https://github.com/ownthink/Jiagu

import jiagu

text = """作为中国银行业龙头和世界资产规模第一大行，工商银行金融牌照齐全，拥有强大的客户基础
和市场竞争力。公司专注综合化业务经营，子公司布局完善，并加速金融科技的发展。截至2019 >年末，工商银行已经连续七年蝉联《福布斯》杂志“全球企业2000 强”及《银行家》杂志“全球银行
1000 强”榜首，连续四年位列全球银行品牌价值500 强榜首。公司长期保持稳健经营策略，已经形
成了五项核心竞争力：强大客户基础、低成本负债、完善信贷结构、优质资产和严格风控等。凭借
这些优势，加之不断推进经营转型和金融科技发展，公司能够多次承受疫情等外部风险冲击。"""
words = jiagu.seg(text)
ner = jiagu.ner(words) # 命名实体识别
#print(ner)
for i,element in enumerate(ner):
    if element != "O":
        print(words[i])

keywords = jiagu.keywords(text, 5) # 关键词
print(keywords)

pos = jiagu.pos(words)
print(pos)



for i,element in enumerate(pos):
    print(words[i]+pos[i])





