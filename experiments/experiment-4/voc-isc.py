import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    i_led_green = np.array([9.95, 21.30, 30.0, 40.2, 49.9])
    v_oc_green = np.array([0.38, 0.40, 0.43, 0.44, 0.45])
    i_sc_green = np.array([1.94, 4.10, 5.84, 7.8, 9.73])

    i_led_blue = np.array([10.31, 20.8, 29.6, 40.1, 50.2])
    v_oc_blue = np.array([0.38, 0.41, 0.43, 0.44, 0.45])
    i_sc_blue = np.array([2.09, 4.08, 5.79, 7.78, 9.75])

    plt.title(r'$V_{oc}$ vs $I_{led}$')
    plt.xlabel(r'$I_{led}$ (mA)')
    plt.ylabel(r'$V_{oc}$ (V)')
    plt.plot(i_led_green, v_oc_green, label='Green')
    plt.plot(i_led_blue, v_oc_blue, label='Blue')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

    plt.title(r'$I_{sc}$ vs $I_{led}$')
    plt.xlabel(r'$I_{led}$ (mA)')
    plt.ylabel(r'$I_{sc}$ (V)')
    plt.plot(i_led_green, i_sc_green, label='Green')
    plt.plot(i_led_blue, i_sc_blue, label='Blue')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()