import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    vdc     = np.array([-5 , -4.5, -4 , -3.5, -3 , -2.5, -2 , -1.5, -1 , -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vdut_pp = np.array([108, 108 , 108, 108 , 108, 108 , 108, 108 , 108, 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108])
    vout_pp = np.array([364, 362 , 360, 360 , 358, 356 , 352, 338 , 284, 266 , 248 , 228 , 196 , 180 , 172 , 160 , 152 , 148 , 144, 145, 145, 145, 146, 146, 147, 148, 148, 148, 148, 149, 149, 150, 151, 151, 152, 152, 152])

    f = 100 # 100 kHz
    Rfb = 150 # 150 k
    Cfb = 100 # 100 pF
    Cdut =  (vout_pp / vdut_pp) * Cfb * np.sqrt(1 + 1/(2 * np.pi * 150 * 10 ** 3 * 100 * 10 ** (-12) ** 2))

    plt.title(r"$C_{dut}$ vs $V_{dc}$")
    plt.xlabel(r"$V_{dc}$ (V)")
    plt.ylabel(r"$C_{dut}$ (pF)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(vdc, Cdut)
    plt.show()
