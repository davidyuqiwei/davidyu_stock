#coding=utf-8
from textrank4zh import TextRank4Sentence

def get_key_sents(cont, num=3):
    '''
    根据内容提取摘要，
    num=3,提取三段摘要，
    return: 下划线拼接提取出的摘要
    '''
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=cont, lower=True, source='all_filters')
    key_sents = []
    summarys = []
    for item in tr4s.get_key_sentences(num=num):
        key_sents.append((item.index, item.weight, item.sentence))
    for s in key_sents:
        summarys.append(s[2])
    return '_'.join(summarys)

if __name__ == '__main__':
    content = "行政院拟放宽2岁以下育儿津贴请领门槛，台中市议员杨正中追问市长，是否跟进，连问七次阿公阿妈两千五百元，要不要发，林佳龙并未正面回应。社会局则指出，市府乐见中央扩大托育补助范围，可让中市托育一条龙效果更好，中央政策如果定案，市府将配合办理。(寇世菁报导)(市长，阿公、阿妈育婴亲属照顾津贴二千五百，你要不要发？)台中市政府社会局向议会专案报告托婴中心虐婴事件，议员杨正中手拿中央扩大育儿津贴发放对象，祖父母顾孙也可领育儿津贴的看板，连连追问市长林佳龙，阿公阿妈两千五百元，到底要不要发？连问七次，还拿出签字笔，要求市长签署同意。但林佳龙并未正面回应，满脸尴尬频频转头，避开议员摆在面前的看板。议员李中也指出，阿公阿妈照顾孙，领育婴津贴，才能彻底解决虐婴事件再度发生，要求市府应该从善如流。市府社会局长吕建德随后则表示，议员对中央政策恐有误解，政院规划扩大育儿津贴规模，主要是放宽发放对象，不再限缩发放对象为自行带小孩的家长，并非所谓再发放爷奶津贴，市府乐见中央扩大托育补助范围，相信将让中市的托育一条龙政策的效果更好。中央政策如果定案，台中市府将配合办理。"
    ks = get_key_sents(content.strip(),num=1)
    print(ks)




