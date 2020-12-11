# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

# O(n^2)
def sum_to_k(K, List):
    for i in range(len(List)):
        for j in range(len(List)):
            if K < List[i] or K < List[j]:
                pass
            elif K != List[i] + List[j]:
                pass
            else:
                print(True)
                print(f"{K} = {List[i]} + {List[j]}")
                return True # removing this will return every possible solution
    print(False)
    return False

def sum_to_k1(K, List):
    for i in range(len(List)):
        if K < List[i]: # prevents going in j loop if i value too large
            pass
        else:
            for j in range(len(List)):
                if K != List[i] + List[j]:
                    pass
                else:
                    print(True)
                    print(f"{K} = {List[i]} + {List[j]}")
                    return True # removing this will return every possible solution
    print(False)
    return False

# O(n) or in 1 pass, use caching?
def sum_to_k2(K, List):
    for i in range(len(List)):
        if List[i] + List[i] == K or List[i] + List[i+1] == K or List[i] + List[i-1] == K:
            # if either number with itself or a neighbor sums to K, then true
            print(True)
            return True
        else:
            print(False)
            return False
        # else:



def main():
    print('\ntest_case_1')
    sum_to_k(17, [10, 15, 3, 7])
    print('test_case_2')
    sum_to_k(12, [10, 15, 3, 7])
    print('test_case_3')
    sum_to_k(5, [1, 3, 4, 2])

    print('\ntest_case_1_1')
    sum_to_k2(17, [10, 15, 3, 7])
    print('test_case_2_1')
    sum_to_k2(12, [10, 15, 3, 7])
    print('test_case_3_1')
    sum_to_k2(5, [1, 3, 4, 2])
    print('test_case_4_1')
    sum_to_k2(17, [10, 15, 3, 7, 4, 2, 1])

if __name__ == "__main__":
    main()
