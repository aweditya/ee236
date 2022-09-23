import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    vd_light_blue = np.array([-2.00, -1.50, -0.98, -0.75, -0.50, -0.40, -0.30, -0.26, -0.20, -0.15, -0.08, -0.08, 0.04, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50, 0.51])
    id_light_blue = np.array([-12.55, -12.03, -11.60, -11.48, -11.34, -11.30, -11.29, -11.29, -11.26, -11.24, -11.23, -11.20, -11.13, -11.08, -10.97, -10.74, -10.42, -9.95, -9.10, -7.01, -4.30, -1.99, -0.91, 2.85, 7.16, 8.71, 13.40, 16.87])

    vd_blue = np.array([0.01, 0.05, 0.12, 0.19, 0.24, 0.30, 0.34, 0.39, 0.42, 0.43, 0.44, 0.44, 0.44, 0.45, 0.45, 0.45, 0.45])
    id_blue = np.array([-11.17, -11.12, -10.91, -10.39, -10.11, -9.46, -8.25, -7.20, -5.21, -4.11, -3.78, -3.10, -2.55, -2.01, -1.49, -0.94, -0.77])

    vd_light_green = np.array([-1.99, -1.50, -1.01, -0.75, -0.51, -0.26, -0.14, 0.00, 0.05, 0.08, 0.15, 0.20, 0.25, 0.30, 0.35, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50])
    id_light_green = np.array([-9.91, -9.38, -9.00, -8.85, -8.72, -8.64, -8.57, -8.56, -8.53, -8.49, -8.38, -8.18, -7.88, -7.44, -6.45, -4.35, -3.57, -2.06, -0.53, 0.69, 3.17, 7.16, 10.72, 15.44, 18.80])

    vd_green = np.array([0.00, 0.05, 0.12, 0.18, 0.23, 0.29, 0.33, 0.35, 0.41, 0.42, 0.43, 0.44])
    id_green = np.array([-8.45, -8.41, -8.30, -8.12, -7.60, -7.21, -6.50, -6.02, -3.61, -3.21, -1.59, -0.75])

    plt.title('Superimposing Part 1 and Part 2 (Green Terminal)')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$I_{D}$ (mA)')
    plt.plot(vd_light_green[np.where(id_light_green < 0)], id_light_green[np.where(id_light_green < 0)], label='Part 1')
    plt.plot(vd_green, id_green, label='Part 2')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

    plt.title('Superimposing Part 1 and Part 2 (Blue Terminal)')
    plt.xlabel(r'$V_{D}$ (V)')
    plt.ylabel(r'$I_{D}$ (mA)')
    plt.plot(vd_light_blue[np.where(id_light_blue < 0)], id_light_blue[np.where(id_light_blue < 0)], label='Part 1')
    plt.plot(vd_blue, id_blue, label='Part 2')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
