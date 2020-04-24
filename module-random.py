# "Lucky or Not" Test Project by haad123
# Sample application of module random

import random 
min = 3
max = 10

n = random.randint(min, max)
    # .randint(a, b) returns a random number between the specified min and max values
print(n)

if n == 7:
    print("Lucky!")
elif n == 4: 
    print("Not lucky.")
else:
    pass
