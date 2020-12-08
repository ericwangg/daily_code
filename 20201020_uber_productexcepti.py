# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# What if no division

# faster if faster way to find list prod
def prod_except_i(List):
    Output = []
    Prod = 1
    for i, j in enumerate(List): # gets product of whole list
        Prod *= j
    for i, j in enumerate(List): # divides value at i from prod, adds
        prod_without_i = Prod/j
        Output.append(prod_without_i)
    return Output

# using no division
def prod_except_i2(List):
    Output = []
    for i, j in enumerate(List):
        ListMod = List
        ListMod[i] = 1

        Prod = 1
        for k in ListMod:
            # print(ListMod)
            Prod *= k
        ListMod[i] = j
        # Why does setting ListMod[i] = j change List
        # print(ListMod)
        # print(List)
        # print('\n')
        Output.append(Prod)
    return Output

print("v1")
print(prod_except_i([1,2,3,4,5]))
print(prod_except_i([3,2,1]))
print("v2")
print(prod_except_i2([1,2,3,4,5]))
print(prod_except_i2([3,2,1]))
