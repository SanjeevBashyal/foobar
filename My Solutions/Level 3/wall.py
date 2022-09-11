#prepare the bunnies escape Level 3 Challenge 1
def solution(map):
    map=Main_map(map)
    d0map=Map([[None for j in range(map.w)] for i in range(map.h)])
    d1map=Map([[None for j in range(map.w)] for i in range(map.h)])
    DD=[d0map,d1map]
    val=1
    collect=[]
    etp=(map.h-1,map.w-1)
    stp=(0,0)
    wc=0
    collect.append([stp,wc])
    d0map.insert(stp,1)
    map.wild_card_insert(stp,wc)
    map.insert(stp,None)
    while True:
        next_nodes=[]
        next_nodes_length=[]
        wild_card_list=[]
        for sp,wc in collect[:]:
            val=DD[wc].value(sp)

            nei=map.neighbors(sp,wc)
            if len(nei)==0:
                collect.remove([sp,wc])
                continue
            else:
                nei_point=nei[0]

            next_nodes.append(nei_point)
            next_nodes_length.append(val+1)
            wild_card_list.append(wc)
            
        min_index=next_nodes_length.index(min(next_nodes_length))
        pp=next_nodes[min_index]
        wc=wild_card_list[min_index]
        ln=next_nodes_length[min_index]
        if wc==0:
            if map.value(pp)==1:
                wc=1
            map.insert(pp,None)
        map.wild_card_insert(pp,wc)
        DD[wc].insert(pp,ln)

        # elif map.value(pp)
        collect.append([pp,wc])
        if pp[0]==etp[0] and pp[1]==etp[1]:
            return ln


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
        self.wild_card_map=[[mat[i][j] for j in range(self.w)] for i in range(self.h)]

    def _in_bounds(self,ij):
        i,j=ij
        return 0 <= i < self.h and 0 <= j < self.w

    def _passable(self, ij):
        i, j = ij
        return self.map[i][j] is not None

    def _wildcard_entry(self,ij,wc):
        i,j=ij
        if wc==0:
            wc=2
        return self.wild_card_map[i][j]<wc

    def wild_card_insert(self,ij,val):
        self.wild_card_map[ij[0]][ij[1]]=val


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
e=[0,0,0,0,1,0,1,0,1,0]
f=[0,0,1,0,1,0,1,0,1,0]
g=[0,0,1,0,1,0,1,0,1,0]
h=[0,0,1,0,0,0,1,0,1,0]
i=[0,0,1,0,1,0,1,0,1,0]
j=[0,0,1,0,0,0,1,0,1,0]
k=[0,0,1,1,1,1,1,0,1,0]
l=[0,0,0,0,0,0,0,0,1,0]
m=[0,0,0,0,0,0,0,0,1,0]
n=[0,0,0,0,0,0,0,1,0,0]
mat=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]

# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution(mat))