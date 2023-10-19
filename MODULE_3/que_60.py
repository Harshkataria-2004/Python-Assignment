# How will you set the starting value in generating random numbers? 

import random
random.seed(42)
random_number_1 = random.randint(1, 100)
random_number_2 = random.uniform(0.0, 1.0)

print(random_number_1)
print(random_number_2)
