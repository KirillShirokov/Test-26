import random
from statistics import mean

num_len = round(random.random() * 100)
nums = [random.random() for element in range(num_len)]

num_min = min(nums)
num_max = max(nums)
num_avg = mean(nums)
print(num_min, num_max, num_avg)
