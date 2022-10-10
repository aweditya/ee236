import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    vdc_square     = np.array([-5 , -4.5, -4 , -3.5, -3 , -2.5, -2 , -1.5, -1 , -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vdut_pp_square = np.array([108, 108 , 108, 108 , 108, 108 , 108, 108 , 108, 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108 , 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108])
    vout_pp_square = np.array([364, 362 , 360, 360 , 358, 356 , 352, 338 , 284, 266 , 248 , 228 , 196 , 180 , 172 , 160 , 152 , 148 , 144, 145, 145, 145, 146, 146, 147, 148, 148, 148, 148, 149, 149, 150, 151, 151, 152, 152, 152])

    vdc_circle     = np.array([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vdut_pp_circle = np.array([108 , 108 , 108 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110 , 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110])
    vout_pp_circle = np.array([1080, 1080, 1080, 1080, 1080, 1080, 1060, 1020, 820 , 720 , 680 , 600 , 580 , 540 , 520 , 500 , 500 , 480 , 480, 480, 480, 490, 500, 500, 490, 490, 490, 480, 500])


    f = 100 # 100 kHz
    Rfb = 150 # 150 k
    Cfb = 100 # 100 pF
    Cdut_square =  (vout_pp_square / vdut_pp_square) * Cfb * np.sqrt(1 + 1/(2 * np.pi * 150 * 10 ** 3 * 100 * 10 ** (-12) ** 2))
    Cdut_circle =  (vout_pp_circle / vdut_pp_circle) * 10 ** (-3) * Cfb * np.sqrt(1 + 1/(2 * np.pi * 150 * 10 ** 3 * 100 * 10 ** (-12) ** 2))

    plt.figure("Square MOSCAP of 1mm side length")
    plt.title(r"$C_{dut}$ vs $V_{dc}$: Square MOSCAP of 1mm side length")
    plt.xlabel(r"$V_{dc}$ (V)")
    plt.ylabel(r"$C_{dut}$ (pF)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(vdc_square, Cdut_square)

    plt.figure("Circle MOSCAP of 2mm diameter")
    plt.title(r"$C_{dut}$ vs $V_{dc}$: Circle MOSCAP of 2mm diameter")
    plt.xlabel(r"$V_{dc}$ (V)")
    plt.ylabel(r"$C_{dut}$ (nF)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(vdc_circle, Cdut_circle)
    plt.show()
