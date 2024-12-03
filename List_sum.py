def rec_list_sum(datalist):
    total = 0

    for i in datalist:
        if type(i) == type([]):
            total= total + rec_list_sum(i)
        else:
            total = total + i
    return total 


print(rec_list_sum([1,2,3,[3,4,3,4,3],[4,5]]))