# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
#
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
#
# Do this in O(N) time.

import time

# using Kadane's Algorithm O(n)
def maxSubArray(L):
    start_time = time.time()

    max = float('-inf') # max value up to this point, starts at -inf, not 0
    sum = 0 # sum for this loop
    for i in L:
        sum += i
        if max <= sum:
            max = sum
        if sum < 0:
            sum = 0
    print(max)
    total_time = time.time() - start_time
    print(f"\nTime taken: {total_time}")
    return(max)

def maxSubArray2(L): # using the max function this time
    start_time = time.time()

    max_val = float('-inf') # max value up to this point, starts at -inf, not 0
    sum = 0 # sum for this loop
    for i in L:
        sum = max(0, sum + i)
        max_val = max(sum, max_val)
    print(max_val)
    total_time = time.time() - start_time
    print(f"\nTime taken: {total_time}")
    return(max_val)


# def main(L):
#     return maxSubarrayQuad(L)
#     return maxSubarrayLin(L)


if __name__ == "__main__":
    print("[34, -50, 42, 14, -5, 86]")
    maxSubArray([34, -50, 42, 14, -5, 86])
    print("[34, -50, 42, 14, -5, 86] using max()")
    maxSubArray2([34, -50, 42, 14, -5, 86])
    # 1st method returns -1, while 2nd method with max() returns 0
    print("\n[-5, -1, -8, -9]")
    maxSubArray([-5, -1, -8, -9])
    print("\n[-5, -1, -8, -9] using max()")
    maxSubArray2([-5, -1, -8, -9])
    # Same thing occurs where the 1st method should be correct and max = only sum in array even if neg number
    print("\n[-23456789]")
    maxSubArray([-23456789])
    print("\n[-23456789] using max()")
    maxSubArray2([-23456789])

    print("\n[1]")
    maxSubArray([1])
    print("\n[1] using max()")
    maxSubArray2([1])

    print("\n[0]")
    maxSubArray([0])
    print("\n[0] using max()")
    maxSubArray2([0])
