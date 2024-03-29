text='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#1.把Text中的better换成worse
text1=text.replace("better","worse")
print(text1)
#2.把Text1中单词包含ea的剔除
text2=text1.split()
text3=[]
for a in text2:
    if 'ea' not in a:
        text3.append(a)
#print(text3)
text4=(' '.join(text3))
print(text4)
text5=text4.swapcase()
print(text5)
print(sorted(text5.split(), key=str.lower))