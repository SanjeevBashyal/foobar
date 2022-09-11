#Level 2 Challenge 2 Don't Get Volunteered
def solution(s,d):
    map=Essential([[0 for j in range(8)] for i in range(8)])
    dmap=Essential([[0 for j in range(8)] for i in range(8)])
    d_ij=map.loc_to_ij(d)
    s_ij=map.loc_to_ij(s)
    if map.check([s_ij],d_ij):
        return 0
    val=1
    collect=[]
    while True:
        nei=map.neighbors(s_ij)
        collect.extend(nei)
        chk=map.check(nei,d_ij)
        if chk:
            return val
        map.update_val(nei,None)
        dmap.update_val(nei,val)
        s_ij=collect.pop(0)
        val=dmap.value(s_ij)+1



class Essential:
    def __init__(self,mat):
        self.map=mat

    def value(self,ij):
        return self.map[ij[0]][ij[1]]

    def _in_bounds(self,ij):
        i,j=ij
        return 0 <= i < 8 and 0 <= j < 8

    def _passable(self, ij):
        i, j = ij
        return self.map[i][j] is not None

    def is_valid(self, ij):
        return self._in_bounds(ij) and self._passable(ij)

    def neighbors(self,ij):
        i,j=ij
        results = [(i+2,j+1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i-2,j-1),(i-1,j-2),(i+1,j-2),(i+2,j-1)]
        results = list(filter(self.is_valid, results))
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

    def update_val(self,ijs,val):
        for ij in ijs:
            self.map[ij[0]][ij[1]]=val
        return True
        

    def check(self,ijs,d_ij):
        for ij in ijs:
            if ij[0]==d_ij[0] and ij[1]==d_ij[1]:
                return True
        return False


print(solution(0, 0))