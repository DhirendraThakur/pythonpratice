import matplotlib.pyplot as plt
import numpy as np
amount = 15
new_list = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(new_list)
for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, new_list)
        plt.pause(0.01)
        plt.clf()
    if new_list[j]>new_list[j+1]:
        new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
plt.show()