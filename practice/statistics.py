import numpy as num
def stats(nums):
    total = sum(nums)
    minimum = min(nums)
    maximum = max(nums)
    average = total/len(nums)

    print("Total sum: ", total)
    print("Minimum: ", minimum)
    print("Maximum: ", maximum)
    print("Average: ", average)

numbers = [0, 1, 5, 17, -6, 18]
stats(numbers)
