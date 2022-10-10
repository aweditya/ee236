import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    vpd_dark = np.array([-4.230, -4.13, -3.890, -3.300, -2.980, -2.530, -2.160, -2.010, -1.450, -1.030, -0.830, -0.680, -0.600, -0.520, -0.490, -0.400, -0.350, -0.300, -0.260, -0.240, -0.100, 0.100, 0.240, 0.260, 0.280, 0.290, 0.320, 0.330, 0.340, 0.350, 0.360, 0.420, 0.450, 0.500, 0.540, 0.600])
    ipd_dark = np.array([-0.000, -0.000, -0.000, -0.000, -0.000, -0.000, -0.000, -0.003, -0.003, -0.003, -0.003, -0.003, -0.003, -0.003, -0.003, -0.002, -0.003, -0.002, -0.003, -0.002, -0.003, 0.000, 0.000, 0.005, 0.010, 0.016, 0.045, 0.057, 0.079, 0.089, 0.124, 0.430, 0.710, 1.510, 2.770, 4.880])

    plt.title(r'Dark I-V Characteristic of Photodiode')
    plt.xlabel(r'$V_{pd}$ (V)')
    plt.ylabel(r'$I_{pd}$ (mA)')
    plt.plot(vpd_dark, ipd_dark)

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

    plt.title(r'Dark Log I-V Characteristic of Photodiode')
    plt.xlabel(r'$V_{pd}$ (V)')
    plt.ylabel(r'$\log{I_{pd}}$')
    plt.plot(vpd_dark, np.log(np.abs(ipd_dark)))

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

    print("Ideality Factor (0.1V - 0.4V) = ", (0.450 - 0.280)/(0.0256 * np.log(0.71/0.01)))
