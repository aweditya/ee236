import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    vd_blue = np.array([0.01, 0.05, 0.12, 0.19, 0.24, 0.30, 0.34, 0.39, 0.42, 0.43, 0.44, 0.44, 0.44, 0.45, 0.45, 0.45, 0.45])
    id_blue = np.array([-11.17, -11.12, -10.91, -10.39, -10.11, -9.46, -8.25, -7.20, -5.21, -4.11, -3.78, -3.10, -2.55, -2.01, -1.49, -0.94, -0.77])
    power_blue = np.abs(vd_blue * id_blue)
    imp_blue = id_blue[np.argmax(power_blue)]
    vmp_blue = vd_blue[np.argmax(power_blue)]
    print(imp_blue, vmp_blue)

    vd_green = np.array([0.00, 0.05, 0.12, 0.18, 0.23, 0.29, 0.33, 0.35, 0.41, 0.42, 0.43, 0.44])
    id_green = np.array([-8.45, -8.41, -8.30, -8.12, -7.60, -7.21, -6.50, -6.02, -3.61, -3.21, -1.59, -0.75])
    power_green = np.abs(vd_green * id_green)
    imp_green = id_green[np.argmax(power_green)]
    vmp_green = vd_green[np.argmax(power_green)]
    print(imp_green, vmp_green)

    plt.title(r'Solar Cell as Power Source (Blue terminal)')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$I_{D}$ (mA), $P_{D}$ (mW)')
    plt.plot(vd_blue, id_blue, label=r'$I_{D}$')
    plt.plot(vd_blue, power_blue, label=r'$P_{D}$')
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

    plt.title(r'Solar Cell as Power Source (Green terminal)')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$I_{D}$ (mA), $P_{D}$ (mW)')
    plt.plot(vd_green, id_green, label=r'$I_{D}$')
    plt.plot(vd_green, power_green, label=r'$P_{D}$')
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
