# ass 1 -- even numbers by 10 and odd numbers by 5 -- and sort them

def inc_num_odd_even(n):
    if n % 2 == 0:
        return n + 10
    else:
        return n + 5
num_list = [1,2,3,4,5,6,7]

for nums in sorted(num_list, key = inc_num_odd_even):
    print(nums)
