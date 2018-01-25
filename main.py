import jieba #結巴中文模組

#----------------------------------
# 停用詞
#----------------------------------

stop_words = []

with open('stop.txt','r',encoding='UTF-8') as file: #把它打開並賦予他一個名字為file2 只能在這使用(區域變數)

    for stop_data in file.readlines(): #停用詞迭代
        stop_data = stop_data.strip()
        stop_words.append(stop_data)


#----------------------------------
# 文章
#----------------------------------

seg_list = []

with open('data.txt','r',encoding='UTF-8') as file:
    data = file.read() #把讀到的資料丟到data裡
    seg_list = jieba.cut(data) #用結巴裡面的cut函式


#----------------------------------
# 文章-停用詞
#----------------------------------

words = []

for words_can in seg_list:
    if words_can not in stop_words:
        words.append(words_can)


#print(words)


#----------------------------------
# 正向情緒詞
#----------------------------------

positives = []

with open('positives.txt','r',encoding='UTF-8') as file:

    for positives_can in file.readlines():
        positives_can = positives_can.strip()
        positives.append(positives_can)

posWords = []
for posWords_can in words:
    if posWords_can in positives:
        posWords.append(posWords_can)

print(posWords)

#----------------------------------
# 負向情緒詞
#----------------------------------

negatives = []

with open('negatives.txt', 'r', encoding='UTF-8') as file:

    for negatives_can in file.readlines():
        negatives_can = negatives_can.strip()
        negatives.append(negatives_can)

negWords = []
for negWords_can in words:
    if negWords_can in negatives:
        negWords.append(negWords_can)

print(negWords)

print('Positive can：', len(posWords))
print('Negatives can：', len(negWords))
print('total word：', len(words))
