nums = [1,2,3,4,5,6,7,8,9,10]

my_list = [n for n in nums if n in range(0,len(nums) + 1,2)]
print(my_list)