def solution(mat):
    map=Main_map(mat)
    val=map.h*map.w
    tree=[]
    tree_val=[]
    tree_index=[]
    tree_wild_card=[]
    stp=(0,0)
    etp=(map.h-1,map.w-1)
    
    tree.append(stp)
    tree_val.append(map.value(stp))
    map.insert(stp,None)
    tree_wild_card.append(1)
    nei=map.neighbors(stp,1)
    if len(nei)>0:
        tree_index.append(0)
    while True:
        if not tree_index[-1]<len(nei):
            map.insert(tree.pop(),tree_val.pop())
            if len(tree)==0:
                break
            tree_wild_card.pop()
            tree_index.pop()
            tree_index[-1]=tree_index[-1]+1
            nei=map.neighbors(tree[-1],tree_wild_card[-1])
            continue
        sub_tree=nei[tree_index[-1]]
        tree.append(sub_tree)
        tree_val.append(map.value(sub_tree))
        map.insert(sub_tree,None)

        if sub_tree[0]==etp[0] and sub_tree[1]==etp[1]:
            l=len(tree)
            if val>l:
                val=l
            map.insert(tree.pop(),tree_val.pop())
            tree_index[-1]=tree_index[-1]+1
            nei=map.neighbors(tree[-1],tree_wild_card[-1])
            continue

        if tree_wild_card[-1]==1:
            if tree_val[-1]==1:
                tree_wild_card.append(0)
            else:
                tree_wild_card.append(1)
        else:
            tree_wild_card.append(0)
        
        nei=map.neighbors(sub_tree,tree_wild_card[-1])
        tree_index.append(0)
    return val



class Map:
    def __init__(self,mat):
        self.map=mat
        self.h=len(self.map)
        self.w=len(self.map[0])

    def value(self,ij):
        return self.map[ij[0]][ij[1]]

    def insert(self,ij,val):
        self.map[ij[0]][ij[1]]=val

    def update_val(self,ijs,val):
        for ij in ijs:
            self.map[ij[0]][ij[1]]=val
        return True

    def check(self,ijs,d_ij):
        for ij in ijs:
            if ij[0]==d_ij[0] and ij[1]==d_ij[1]:
                return True
        return False

class Main_map(Map):
    def __init__(self, mat):
        Map.__init__(self,mat)

    def _in_bounds(self,ij):
        i,j=ij
        return 0 <= i < self.h and 0 <= j < self.w

    def _passable(self, ij):
        i, j = ij
        return self.map[i][j] is not None

    def _wildcard_entry(self,ij,wc):
        i,j=ij
        return self.map[i][j]<=wc


    def is_valid(self, ij,wc):
        return self._in_bounds(ij) and self._passable(ij) and self._wildcard_entry(ij,wc)

    def neighbors(self,ij,wc):
        i,j=ij
        results = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        results = list(filter(lambda ij:self.is_valid(ij,wc), results))
        return results

    def ij_to_loc(self,ij):
        i,j=ij
        return i*8+j

    def ijs_to_locs(self,ijs):
        out=[]
        for ij in ijs:
            out.append(self.ij_to_loc(ij))
        return out

    def loc_to_ij(self,loc):
        i=loc/8
        j=loc%8
        return (i,j)

a=[0,0,1,0,0,1,1,0,0,0]
b=[1,0,0,0,1,0,1,0,1,0]
c=[0,1,1,1,1,0,1,0,1,0]
d=[1,1,1,1,0,0,1,0,1,0]
e=[1,0,0,0,1,0,1,0,1,0]
f=[1,0,1,0,1,0,1,0,1,0]
g=[1,0,1,0,1,0,1,0,1,0]
h=[1,0,1,0,0,0,1,0,1,0]
i=[1,0,1,0,1,0,1,0,1,0]
j=[1,0,1,0,0,0,1,0,1,0]
k=[1,0,1,1,1,1,1,0,1,0]
l=[1,0,0,0,0,0,0,0,1,0]
m=[1,1,1,1,1,1,1,0,1,0]
n=[1,1,1,1,1,1,1,1,0,0]
mat=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]

# print(solution(mat))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
]))