#Level 2 Challenge 1 Ion Flux Relabeling
import math as m
def solution(h,q):
    out=[]
    for i in q:
        add=0
        n=m.log(i+1,2)
        while True:
            p=n
            b=int(p)
            if b>=h:
                out.append(-1)
                break
            if p==b or b==1:
                add=add+2**(b+1)-1
                out.append(add)
                break
            i=i+1-2**b
            n=m.log(i+1,2)
            if n<b:
                add=add+2**b-1

    return out
    # pass
    # return 4

solution(5, [19, 14, 28])
# s(3, [7, 3, 5, 1])