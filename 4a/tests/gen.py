import sys
from random import randint, random, choices
from string import printable
from struct import pack

def mid(l):
    return round(sum(l) / len(l))

def sorr(l, s):
    if(len(l) == 0):
        return
    r = len(l) // 2
    s.append(l[r])

    sorr(l[:r], s)
    sorr(l[r+1:], s)
    return

n = sys.argv[1]
k = int(sys.argv[2])
name = sys.argv[3]
f = open(name+".txt", "w")
g = open(name+"_sorted.txt", "w")

t = []
if(n[0] == "-"):
    #l = [0,8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
    #for i in l[1:]:
    #    l.append(-i)
    l = list(range(-k, k+1))
    t = list(range(-k, k+1))

else:
    l = [randint(-k, k) for i in range(k)]
    for i in l:
        t.append(i)

t.sort()
so = []
sorr(t, so)

ll = []
for i in l:
    ll.append("add")
    ll.append(str(i))
    ll.append("".join(choices(printable[:62], k=2)))
    ll.append(str(random()))
ll.append("exit")
ll.append("ge")
f.write("\n".join(ll))
f.close()

ll = []
for i in so:
    ll.append("add")
    ll.append(str(i))
    ll.append("".join(choices(printable[:62], k=2)))
    ll.append(str(random()))
ll.append("exit")
ll.append("gwew")
g.write("\n".join(ll))
g.close()
