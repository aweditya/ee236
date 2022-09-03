import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def linear(x, m, c):
    return m * x + c

if __name__ == '__main__':
    Rfb = 8.2 # 8.2k
    Cfb = 390 # 390 pF
    f = 10e6  # 1 MHz

    vdut = np.array([14, 16, 16.4, 16.6, 16.8, 17, 17.2, 17, 16.8, 17, 17, 16.8, 16.6, 16.6, 16.6, 16.6, 17, 17, 17.2, 17.2, 17.2])
    vout = np.array([17.8, 17, 14.4, 12.8, 11.6, 10.6, 9.8, 9.2, 8.4, 8.2, 7.8, 7.6, 7.4, 7, 6.8, 6.6, 6.6, 6.2, 6.2, 6.2, 6.2])

    assert vdut.shape == vout.shape
    cdut = (vout / vdut) * (Cfb * 10 ** -12) * np.sqrt(1 + 1/(2 * np.pi * (f * 10 ** 6) * (Rfb * 10 ** 3) * (Cfb * 10 ** -12)) ** 2)

    vdc = np.linspace(0, 10, 21)

    plt.title(r'$C_{dut}$ vs $V_{dc}$')
    plt.xlabel(r'$V_{dc}$ (V)')
    plt.ylabel(r'$C_{dut}$ $(pF)$')
    plt.plot(-vdc, cdut * 10 ** 9)
    plt.show()

    plt.title(r'$1/C_{dut}^{2}$ vs $V_{dc}$')
    plt.xlabel(r'$V_{dc}$ (V)')
    plt.ylabel(r'$\frac{1}{C_{dut}^{2}}$ $(pF^{-2})$')
    plt.plot(-vdc, 1/ (cdut * 10 ** 9) ** 2)
    plt.show()

    popt, _ = curve_fit(f = linear, xdata = -vdc, ydata = 1 / (cdut * 10 ** 9) ** 2)
    print(popt)
    # m = 4.9677357, c = 4.51693647
