# NumPy Random Numbers

import numpy as np

random_nums = np.random.randint(1, 100, size=5)

print("Random Numbers:", random_nums)
print("Maximum:", np.max(random_nums))
print("Minimum:", np.min(random_nums))
print("Average:", np.mean(random_nums))
