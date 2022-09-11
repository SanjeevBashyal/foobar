#Level 5 Challenge 1 Expanding Nebula
def solution(g):
    g = list(zip(*g))
    nrows=len(g)
    ncols=len(g[0])
    ncols_one_less=ncols-1
    decimal_g=[sum([1<<(ncols_one_less-j) for j,ele in enumerate(row) if ele==True]) for row in g]
    total_row_possibilities=1<<(ncols+1)
    total=dict()
    for i in range(total_row_possibilities):
        for j in range(total_row_possibilities):
            output_row=next_state_of_two_rows(i,j,ncols)
            if output_row in decimal_g:
                if output_row in total:
                    if i in total[output_row]:
                        total[output_row][i].add(j)
                    else:
                        total[output_row][i]={j}
                else:
                    total[output_row]={i:{j}}

    collect={i:1 for i in range(total_row_possibilities)}
    for k in range(nrows):
        collect_next=dict()
        for i in collect:
            if i in total[decimal_g[k]]:
                list_of_possible_next_rows=total[decimal_g[k]][i]
                for j in list_of_possible_next_rows:
                    if j in collect_next:
                        collect_next[j]+=collect[i]
                    else:
                        collect_next[j]=collect[i]
        collect=collect_next
    return sum(collect.values())

def next_state_of_two_rows(row1,row2,ncols):
    a11=row1
    a12=row1<<1
    a21=row2
    a22=row2<<1
    only_one_in_four_is_one= ~((~a11 | a12 | a21 | a22) & (a11 | ~a12 | a21 | a22) & (a11 | a12 | ~a21 | a22) & (a11 | a12 | a21 | ~a22))
    clipped_to_ncols=only_one_in_four_is_one&((1<<(ncols+1))-1)
    clipped_to_ncols_minus_1=clipped_to_ncols>>1
    return clipped_to_ncols_minus_1

# print(solution([[True,False]]))
# print(solution([[True, False, True], [False, True, False], [True, False, True]]))
print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))
# print(solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]))
# print(next_state_of_two_rows(0,14,3))