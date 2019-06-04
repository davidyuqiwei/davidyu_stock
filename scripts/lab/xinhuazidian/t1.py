## data dir is 
#  /home/davidyu/gits/chinese-xinhua/data

f = open("ci.csv","rb")
line=f.readline()
a1=[]
while line:
    line = f.readline()
    a1.append(line)
    
    
ci_list = [x.decode("utf-8") for x in a1]

ci_list=[]
for x in a1:
    try: 
        ci_list.append(x.decode("utf-8"))
    except:
        pass



import json
f = open("word.json", encoding='utf-8')
word_list = json.load(f)

a1=word_list[0]
ch_word=[x['word'] for x in word_list]









