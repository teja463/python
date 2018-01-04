import functools

palind = lambda s: s==s[::-1]
s_list = ["radar", "teja", "malayalam", "pramod"]
palind_list = map(palind, s_list)
print (list(palind_list))

even_lambda = lambda x: x%2 == 0
odd_lambda = lambda x: x%2 !=0

sample_list = [1,2,3,4,5,6,7,8,9,10]
print ("all elements", sample_list)

even_list = list(filter(even_lambda, sample_list))
odd_list = list(filter(odd_lambda, sample_list))
print ("even elements", even_list)
print ("odd elements", odd_list)


l_sum_of_nums = lambda num1, num2: num1 +num2
sum_of_nums = functools.reduce(l_sum_of_nums, range(1,6))
print (sum_of_nums)
