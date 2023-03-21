import random
import math

def generate(n):
    nums = [False, False]
    nums += [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i]:
            j = 0
            while (i ** 2) + (j * i) <= n:
                nums[(i ** 2) + (j * i)] = False
                j += 1
    return nums

a = generate(10000000)
