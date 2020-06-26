
#import random

rand_num = random.choice(range(3) or [1000, 4])

print(rand_num)

rand_num = random.randint(0, 10000)

print(rand_num)

print(dir(random.randint))