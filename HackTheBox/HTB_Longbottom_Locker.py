#!/usr/bin/python3
import sys
import pickle

f = open(sys.argv[1], 'rb')
mydict = pickle.load(f)
f.close

for i in mydict:
    b=[]
    for x in i:
        b.append(x[0] * x[1])

    print("".join(b))
