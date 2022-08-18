import random
from statistics import mean

num_len = round(random.random() * 100)
nums = [random.random() for element in range(num_len)]
# nums = array('f', [])
# while count != num2:
#     num3 = random.random()
#     count = count + 1
#     nums.append(num3)

num_min = min(nums)
num_max = max(nums)
num_avg = mean(nums)
print(num_min, num_max, num_avg)
