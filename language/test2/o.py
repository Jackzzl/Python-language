from nltk.corpus import gutenberg
#macbeth_sentences= gutenberg.sents('shakespeare-macbeth.txt')
#print(macbeth_sentences)
"""
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
"""
"""
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])
"""
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')
