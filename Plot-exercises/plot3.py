import matplotlib.pyplot as plt
import numpy as np

def plot_funtion():

    x = np.linspace(-10,10, 500)
    y = np.arctan(x)

    plt.figure(figsize =(10,6))
    plt.plot(x,y, color = "purple", label="$f(x) = arctg(x)")

    plt.legend()
    plt.title('Graph of the Function $f(x) = arctg(x)')
    plt.xlabel('x-axis')
    plt.ylabel('f(x)')
    plt.grid(True)

    plt.show()

plot_funtion()
