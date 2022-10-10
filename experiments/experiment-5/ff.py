import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    temp = np.array([35, 45, 55, 65, 75])
    ff = np.array([0.6721, 0.6518, 0.6176, 0.5971, 0.5777])

    plt.title("FF vs Temperature")
    plt.xlabel(r"Temperature $^{\circ}C$")
    plt.ylabel("FF")
    plt.plot(temp, ff)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
