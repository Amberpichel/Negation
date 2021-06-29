import nltk
from collections import Counter
import sys

count = Counter()
with open(sys.argv[1]) as doc:
    count.update(nltk.word_tokenize(doc.read().lower()))

print ("'afwezig' occurred", count['afwezig'], "times")
print ("'geen' occurred", count['geen'], "times")
print ("'niet' occurred", count['niet'], "times")
print ("'niets' occurred", count['niets'], "times")
print ("'nooit' occurred", count['nooit'], "times")
print ("'niks' occurred", count['niks'], "times")
print ("'zonder' occurred", count['zonder'], "times")
print ("'niemand' occurred", count['niemand'], "times")
print ("'weigeren' occurred", count['weigeren'], "times")
print ("'prevent' occurred", count['prevent'], "times")
print ("'noch' occurred", count['noch'], "times")