import numpy as np
import matplotlib.pyplot as plt

numbers = np.loadtxt('values_for_hist.csv', delimiter = ',', dtype=int)

plt.hist(numbers,bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Value Ranges")
plt.ylabel("Frequencies")
plt.title("Histogram of Real Numbers")
plt.legend()
plt.show()