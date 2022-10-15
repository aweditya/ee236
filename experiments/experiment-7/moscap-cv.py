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
    Cdut_circle =  (vout_pp_circle / vdut_pp_circle) * Cfb * np.sqrt(1 + 1/(2 * np.pi * 150 * 10 ** 3 * 100 * 10 ** (-12) ** 2))

    plt.figure("Square MOSCAP of 1mm side length")
    plt.title(r"$C_{dut}$ vs $V_{dc}$: Square MOSCAP of 1mm side length")
    plt.xlabel(r"$V_{dc}$ (V)")
    plt.ylabel(r"$C_{dut}$ (pF)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(vdc_square, Cdut_square)

    plt.figure("Circle MOSCAP of 2mm diameter")
    plt.title(r"$C_{dut}$ vs $V_{dc}$: Circle MOSCAP of 2mm diameter")
    plt.xlabel(r"$V_{dc}$ (V)")
    plt.ylabel(r"$C_{dut}$ (pF)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(vdc_circle, Cdut_circle)
    plt.show()

    q = 1.6 * 10 ** (-19)
    eox = 3.9
    esi = 11.7
    e0 = 8.85 * 10 ** (-12)

    A_square = 10 ** (-6)
    Cox_square = Cdut_square[np.where(Cdut_square > 300)].mean()
    Cmin_square = Cdut_square[np.where(Cdut_square < 150)].mean()
    tox_square = A_square * eox * e0 / (Cox_square * 10 ** (-12))
    Cs_square = 1/(1/Cmin_square - 1/Cox_square)
    tdep_square = A_square * esi * e0 / (Cs_square * 10 ** (-12))
    print("Square MOSCAP")
    print("Cox =", Cox_square)
    print("tox =", tox_square)
    print("Cmin =", Cmin_square)
    print("Cs =", Cs_square)
    print("tdep =", tdep_square)

    A_circle = np.pi * 10 ** (-6)
    Cox_circle = Cdut_circle[np.where(Cdut_circle > 950)].mean()
    Cmin_circle = Cdut_circle[np.where(Cdut_circle < 450)].mean()
    tox_circle = A_circle * eox * e0 / (Cox_circle * 10 ** (-12))
    Cs_circle = 1/(1/Cmin_circle - 1/Cox_circle)
    tdep_circle = A_circle * esi * e0 / (Cs_circle * 10 ** (-12))
    print("Circle MOSCAP")
    print(Cdut_circle)
    print("Cox =", Cox_circle)
    print("tox =", tox_circle)
    print("Cmin =", Cmin_circle)
    print("Cs =", Cs_circle)
    print("tdep =", tdep_circle)
