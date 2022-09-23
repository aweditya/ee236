from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    vd_35 = np.array([0.025, 0.054, 0.11, 0.153, 0.192, 0.227, 0.304, 0.349, 0.4, 0.425])
    id_35 = np.array([0.002, 0.007, 0.025, 0.052, 0.094, 0.162, 0.521, 1.048, 2.42, 3.75])

    vd_45 = np.array([0.054, 0.1, 0.196, 0.242, 0.271, 0.3, 0.314, 0.343, 0.372, 0.402])
    id_45 = np.array([0.012, 0.02, 0.14, 0.29, 0.441, 0.71, 0.874, 1.39, 2.24, 3.84])

    vd_55 = np.array([0.035, 0.098, 0.156, 0.202, 0.246, 0.292, 0.318, 0.342, 0.358, 0.379])
    id_55 = np.array([0.008, 0.037, 0.098, 0.204, 0.400, 0.829, 1.279, 1.95, 2.55, 3.87])

    vd_65 = np.array([0.053, 0.123, 0.177, 0.235, 0.262, 0.284, 0.309, 0.329, 0.345, 0.354])
    id_65 = np.array([0.017, 0.073, 0.171, 0.435, 0.74, 0.996, 1.523, 2.19, 2.92, 3.53])

    vd_75 = np.array([0.055, 0.113, 0.165, 0.220, 0.260, 0.279, 0.291, 0.309, 0.324, 0.334])
    id_75 = np.array([0.024, 0.085, 0.205, 0.502, 0.972, 1.40, 1.77, 2.37, 3.18, 3.84])

    plt.title("I-V Characteristics in Dark Condition")
    plt.grid((True))
    plt.plot(vd_35, id_35, label=r"$35^{\circ}$C") 
    plt.plot(vd_45, id_45, label=r"$45^{\circ}$C")
    plt.plot(vd_55, id_55, label=r"$55^{\circ}$C")
    plt.plot(vd_65, id_65, label=r"$65^{\circ}$C")
    plt.plot(vd_75, id_75, label=r"$75^{\circ}$C")
    plt.xlabel(r"$V_{d}$ (V)")
    plt.ylabel(r"$I_{d}$ (mA)")
    plt.legend()
    plt.show()

    plt.title("ln(I)-V Characteristics in Dark Condition")
    plt.plot(vd_35, np.log(id_35), label=r"$35^{\circ}$C") 
    plt.plot(vd_45, np.log(id_45), label=r"$45^{\circ}$C")
    plt.plot(vd_55, np.log(id_55), label=r"$55^{\circ}$C")
    plt.plot(vd_65, np.log(id_65), label=r"$65^{\circ}$C")
    plt.plot(vd_75, np.log(id_75), label=r"$75^{\circ}$C")
    plt.grid((True))
    plt.xlabel(r"$V_{d}$ (V)")
    plt.ylabel(r"$\ln{\left(I_{d}\right)}$")
    plt.legend()
    plt.show()