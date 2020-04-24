# "Lucky or Not?" test project by haad123
# sample application of module random

import random 
min = 3
max = 10

n = random.randint(min, max)
print(n)

if n == 7:
    print("Lucky!")
elif n == 4: 
    print("Not lucky.")
else:
    pass