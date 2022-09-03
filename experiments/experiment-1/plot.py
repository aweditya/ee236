import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # 1N914 PN diode
    pn_v = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.71, 0.72, 0.75, 0.77, 0.8, 0.82, 0.85])
    pn_i = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 1.1, 2.8, 5.3, 10, 18.3])

    # BAT85 Schottky Diode
    bat_v = np.array([0.1, 0.15, 0.2, 0.25, 0.28, 0.3, 0.32, 0.34, 0.35, 0.38, 0.4, 0.42, 0.44, 0.45])
    bat_i = np.array([0, 0, 0, 0, 0, 0, 0, 0.6, 1.7, 5, 8.1, 11.8, 17.6, 20.5])

    # Zener Diode
    zener_v = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.81, 0.82, 0.83, 0.85, 0.87, 0.89])
    zener_i = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.8, 1.3, 3.2, 8.2, 18.3])

    # Red LED
    red_v = np.array([0, 0.5, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.85, 1.88, 1.9, 1.95, 1.97, 2])
    red_i = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 1.3, 4.3, 8.1, 12.6])

    # Green LED
    green_v = np.array([0, 0.5, 1, 1.5, 2, 2.5, 2.52, 2.55, 2.58, 2.6, 2.65, 2.7, 2.8, 2.9, 3, 3.04])
    green_i = np.array([0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.2, 0.5, 0.8, 1.4, 2.4, 4.3, 6.2, 6.8])

    # Blue LED
    blue_v = np.array([0, 0.5, 1, 1.5, 2, 2.5, 2.6, 2.65, 2.7, 2.71, 2.73, 2.75, 2.8, 2.83, 2.85, 2.88])
    blue_i = np.array([0, 0, 0, 0, 0, 0, 0, 0.1, 0.9, 1.1, 1.4, 2.1, 4.3, 5.7, 6.8, 8.1])

    # White LED
    white_v = np.array([0, 0.5, 1, 1.5, 2, 2.4, 2.7, 2.76, 2.8, 2.82, 2.84, 2.86, 2.88, 2.9, 2.95])
    white_i = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2.8, 3.4, 4.4, 5.3, 7.5])

    plt.plot(pn_v, pn_i, label = '1N914')
    plt.plot(bat_v, bat_i, label = 'BAT85')
    plt.plot(zener_v, zener_i, label = 'Zener')
    plt.plot(red_v, red_i, label = 'Red LED', color='red')
    plt.plot(green_v, green_i, label = 'Green LED', color='green')
    plt.plot(blue_v, blue_i, label = 'Blue LED', color='blue')
    plt.plot(white_v, white_i, label = 'White LED', color='black')

    plt.title('I-V Characteristic')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (mA)')
    plt.legend()
    plt.show()

    plt.plot(pn_v, np.log(pn_i * 10 ** -3), label = '1N914')
    plt.plot(bat_v, np.log(bat_i * 10 ** -3), label = 'BAT85')
    plt.plot(zener_v, np.log(zener_i * 10 ** -3), label = 'Zener')
    plt.plot(red_v, np.log(red_i * 10 ** -3), label = 'Red LED', color='red')
    plt.plot(green_v, np.log(green_i * 10 ** -3), label = 'Green LED', color='green')
    plt.plot(blue_v, np.log(blue_i * 10 ** -3), label = 'Blue LED', color='blue')
    plt.plot(white_v, np.log(white_i * 10 ** -3), label = 'White LED', color='black')

    plt.title('log(I)-V Characteristic')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Log(Current)')
    plt.legend()
    plt.show()
