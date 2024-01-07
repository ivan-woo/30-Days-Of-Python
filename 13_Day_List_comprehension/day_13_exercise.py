# syntax
arg1 = 5
arg2 = 6
arg3 = 0
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Filter only negative and zero in the list using list comprehension
neg_nums = [num for num in numbers if num <= 0]
print(neg_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(flattened_list)

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)
