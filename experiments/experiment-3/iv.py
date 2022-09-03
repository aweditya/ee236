import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    v_d = np.array([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.302, 0.378, 0.465, 0.495, 0.563, 0.609, 0.618, 0.636, 0.646, 0.702, 0.751, 0.801, 0.850, 0.912, 1.0])
    i_d = np.array([0, 0, 0, 0, 0, 0, 0, 0.001, 0.006, 0.010, 0.027, 0.091, 0.105, 0.142, 0.173, 0.460, 1.140, 3.670, 8.840, 23.60, 69])

    assert v_d.shape == i_d.shape

    plt.title(r'I-V Characteristic of PIN diode')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$I_{D}$ (mA)')
    plt.plot(v_d, i_d)
    plt.show()

    plt.title(r'log(I)-V Characteristic of PIN diode')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$\log(I_{D})$')
    plt.plot(v_d, np.log(i_d))
    plt.show()
