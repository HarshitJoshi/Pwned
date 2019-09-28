import itertools
import trie
import time
from string import ascii_lowercase as lower
f = open("words_alpha.txt", "r")

#WIP: need better generator scheme
words = [x+y+z+t for x in lower for y in lower for z in lower for t in lower]

#words = [x+y for x in lower for y in lower]

root = trie.Trie()
for word in f:
    root.insert(word)

'''c = 0
for m in metric:
    c = c + 1'''

count = 0
start = time.time()
for a in words:
    for w in root.get_possible_words(a):
        if (w == a):
            count = count + 1
end = time.time()
print(end-start)
print(count)

