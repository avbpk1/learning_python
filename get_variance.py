# create a function that takes a collection/list of numbers and returns variance of the list.
def get_variance(*args):
    num_coll = []
    sum_coll = cnt_coll = sum_sqr_diffs = 0
    
    for v in args:
        num_coll.append(v)
        sum_coll += v
        cnt_coll += 1
    mean = sum_coll/cnt_coll
    
    for i in num_coll:
        sum_sqr_diffs += ((i - mean)**2)
        
    return sum_sqr_diffs/(cnt_coll-1)

var_col1 = get_variance(10,20,30)
print(var_col1)
