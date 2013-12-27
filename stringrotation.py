from collections import deque
import sys

with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if line=='':
            continue
        a,b=line.split(',')
        new=deque(a)
        new.rotate(1)
        count=0
        for i in range(len(new)+1):
            new.rotate(1)
            count+=1
            joined=''.join(new)
            if count<len(new)+1:
                if b==joined:
                    print "True"
                    break
            else:
                print "False"
