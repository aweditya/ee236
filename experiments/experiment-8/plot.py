from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # vsd = 200mV
    vsg = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.68, 0.78, 0.87, 0.99, 1.01, 1.18, 1.28, 1.51, 2.03, 2.13, 2.25, 2.43, 2.52, 2.76, 3.01, 3.51, 3.98, 4.50, 4.97])
    id  = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.40, 4.50, 10.3, 11.5, 20.8, 26.5, 36.6, 53.4, 56.3, 59.0, 63.2, 64.9, 69.6, 73.9, 81.3, 87.0, 92.3, 96.5])
    
    # plt.title("PMOS Transfer Characteristics (Linear)")
    # plt.plot(vsg, id, label=r"$V_{SD}$=200mV")
    plt.plot(vsg, np.log(id), label=r"$V_{SD}$=200mV")
    # plt.xlabel(r"$V_{SG}$ (V)")
    # plt.ylabel(r"$\ln(I_{D})$ $({\mu}A)$")
    # plt.grid(True)
    # plt.legend()
    # plt.show()

    # vsd = 5V
    vsg = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.67, 0.75, 1.02, 1.27, 1.520, 1.750, 2.020, 2.260, 2.530, 2.750, 3.010, 3.280, 3.56, 3.73, 4.02, 4.29, 4.52, 4.73, 5.00])
    id  = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.10, 1.10, 17.8, 53.9, 108.8, 172.1, 262.0, 353.0, 471.0, 567.0, 700.0, 843.0, 1003, 1101, 1280, 1452, 1603, 1746, 1930])

    # plt.title("PMOS Transfer Characteristics (Saturation)")
    plt.title("PMOS Transfer Characteristics")
    # plt.plot(vsg, id, label=r"$V_{SD}$=200mV")
    plt.plot(vsg, np.log(id), label=r"$V_{SD}$=5V")
    plt.xlabel(r"$V_{SG}$ (V)")
    plt.ylabel(r"$\ln (I_{D})$ $({\mu}A)$")
    plt.grid(True)
    plt.legend()
    plt.show()

    print("Vt = 0.68V")

    # Part 2: Drain Characteristics
    plt.title("PMOS Drain Characteristics")
    # vsg = 1.5V
    vsd = np.array([0.10, 0.20, 0.31, 0.41, 0.51, 0.75, 1.01, 1.25, 1.53, 2.03, 2.59, 3.03, 3.520, 4.000, 4.510, 4.970])
    id  = np.array([23.6, 43.9, 59.0, 70.7, 78.4, 87.0, 90.0, 91.8, 93.5, 95.9, 98.2, 99.7, 101.3, 102.7, 104.2, 105.3])
    plt.plot(vsd, id, label=r"$V_{SG}$=1.50V")

    # vsg = 2.5V
    vsd = np.array([0.10, 0.20, 0.310, 0.400, 0.500, 0.750, 1.020, 1.260, 1.520, 2.020, 2.560, 3.000, 3.530, 4.000, 4.540, 4.970])
    id  = np.array([49.4, 95.4, 137.2, 171.3, 205.0, 278.0, 336.0, 373.0, 395.0, 413.0, 424.0, 432.0, 439.0, 445.0, 451.0, 456.0])
    plt.plot(vsd, id, label=r"$V_{SG}$=2.50V")

    # vsg = 3.5V
    vsd = np.array([0.10, 0.200, 0.300, 0.400, 0.500, 0.740, 1.010, 1.250, 1.510, 1.750, 2.010, 2.500, 2.970, 3.490, 4.010, 4.520, 4.990])
    id  = np.array([71.6, 137.9, 194.8, 249.0, 304.0, 430.0, 549.0, 641.0, 724.0, 789.0, 841.0, 899.0, 924.0, 945.0, 961.0, 974.0, 985.0])
    plt.plot(vsd, id, label=r"$V_{SG}$=3.52V")
    plt.xlabel(r"$V_{SD}$ (V)")
    plt.ylabel(r"$I_{D}$ $({\mu}A)$")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Part 3: Body Effect (vsd = 200mV)
    plt.title("Body Effect")
    # vsb = -1V
    vsg = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.86, 0.87, 1.02, 1.11, 1.18, 1.22, 1.26, 1.36, 1.51, 1.74, 2.05, 2.270, 2.530, 3.000, 3.550, 4.050, 4.550, 4.980])
    id  = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00, 0.10, 2.90, 7.50, 13.4, 17.2, 20.9, 31.3, 49.3, 71.6, 94.8, 107.5, 120.1, 137.7, 153.0, 164.0, 172.8, 179.4])
    plt.plot(vsg, np.log(id), label=r"$V_{SB}$ = -1V")

    # vsb = -2V
    vsg = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.11, 1.15, 1.20, 1.26, 1.35, 1.49, 1.77, 2.03, 2.550, 3.020, 3.520, 4.030, 4.500, 4.980])
    id  = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 1.90, 3.10, 5.70, 9.60, 17.0, 32.5, 61.8, 82.3, 112.6, 131.4, 146.9, 158.9, 167.8, 175.6])
    plt.plot(vsg, np.log(id), label=r"$V_{SB}$ = -2V")

    # vsb = -3V
    vsg = np.array([0.0, 0.5, 1.1, 1.2, 1.25, 1.31, 1.35, 1.41, 1.50, 1.77, 2.04, 2.540, 3.030, 3.550, 4.050, 4.530, 4.980])
    id  = np.array([0.0, 0.0, 0.1, 1.6, 3.90, 6.20, 9.10, 13.5, 21.8, 51.8, 74.7, 106.2, 126.7, 143.2, 155.5, 165.1, 172.6])
    plt.plot(vsg, np.log(id), label=r"$V_{SB}$ = -3V")
    plt.xlabel(r"$V_{SG}$ (V)")
    plt.ylabel(r"$\ln (I_{D})$ $({\mu}A)$")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.title("Body Effect")
    # vsb = -1V
    vsg = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.86, 0.87, 1.02, 1.11, 1.18, 1.22, 1.26, 1.36, 1.51, 1.74, 2.05, 2.270, 2.530, 3.000, 3.550, 4.050, 4.550, 4.980])
    id  = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00, 0.10, 2.90, 7.50, 13.4, 17.2, 20.9, 31.3, 49.3, 71.6, 94.8, 107.5, 120.1, 137.7, 153.0, 164.0, 172.8, 179.4])
    plt.plot(vsg, id, label=r"$V_{SB}$ = -1V")

    # vsb = -2V
    vsg = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.11, 1.15, 1.20, 1.26, 1.35, 1.49, 1.77, 2.03, 2.550, 3.020, 3.520, 4.030, 4.500, 4.980])
    id  = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 1.90, 3.10, 5.70, 9.60, 17.0, 32.5, 61.8, 82.3, 112.6, 131.4, 146.9, 158.9, 167.8, 175.6])
    plt.plot(vsg, id, label=r"$V_{SB}$ = -2V")

    # vsb = -3V
    vsg = np.array([0.0, 0.5, 1.1, 1.2, 1.25, 1.31, 1.35, 1.41, 1.50, 1.77, 2.04, 2.540, 3.030, 3.550, 4.050, 4.530, 4.980])
    id  = np.array([0.0, 0.0, 0.1, 1.6, 3.90, 6.20, 9.10, 13.5, 21.8, 51.8, 74.7, 106.2, 126.7, 143.2, 155.5, 165.1, 172.6])
    plt.plot(vsg, id, label=r"$V_{SB}$ = -3V")
    plt.xlabel(r"$V_{SG}$ (V)")
    plt.ylabel(r"$I_{D}$ $({\mu}A)$")
    plt.grid(True)
    plt.legend()
    plt.show()