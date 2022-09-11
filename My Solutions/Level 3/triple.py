#Level 3 Challenge 2 Find the access codes
def solution(l):
    triples_num=triples(l)
    return sum([sum(i) for i in triples_num])

def triples(l):
    tree=multiples_tree(l)
    return [[len(tree[j]) for j in i] for i in tree if len(i)>0]

def multiples_tree(l):
    return [multiples(l[i+1:],l[i],i+1) for i in range(len(l))]

def multiples(l,n,offset):
    return [i+offset for i in range(len(l)) if l[i]%n==0]


print(solution([1, 2, 3, 4, 5, 6]))