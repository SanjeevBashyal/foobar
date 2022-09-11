#Level 1 Challenge 1 Skipping Work
def solution(x,y):
    x_set=set(x)
    y_set=set(y)
    if len(x_set)>len(y_set):
        return (x_set-x_set.intersection(y_set)).pop()
    else:
        return (y_set-y_set.intersection(x_set)).pop()
    # pass
    # return 4

solution({1,2},{2})