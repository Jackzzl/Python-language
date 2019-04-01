"""
import re

pattern = re.compile(r'[0-9]{4}')
#time ='2019-03-28'
times =('2019-03-28','03/28/2019','03.2017.28')

#使用刚刚编译好的pattern去匹配time
match = pattern.search(time)
match.group()

for time in times:
    match = pattern.search(time)

    if match:
        print('年份有:',match.group())
"""

#############傅老师
#from nltk.book import *
#import nltk
from nltk.corpus import gutenberg
"""
fdist1 =FreqDist(text1)
#fdist1.plot(50,cumulative =True)
vocabulary1=list(fdist1.keys())
#print(vocabulary1[:50]) 统计最常用的50个字数
print(fdist1['whale'])
"""

#V = set(text1)
#long_words= [w for w in V if len(w)>15]
#print(sorted(long_words))
##emma=nltk.corpus.gutenberg.words('austen-emma.txt')
#print(len(emma))
for fileid in gutenberg.fileids():
    num_chars= len(gutenberg.raw(fileid))#统计字符数
    num_words=len(gutenberg.words(fileid))#单词数
    num_sents=len(gutenberg.sents(fileid))#句子数
    for w in gutenberg.words(fileid):
        w= set(w.lower())
    num_vocab = len(w)
    x=int(num_chars/num_words)
    y=int(num_words/num_sents)
    z=int(num_words/num_vocab)
    print(x,y,z,fileid)

#for fileid in gutenberg.fileids():