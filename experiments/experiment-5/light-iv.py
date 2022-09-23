from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    vl_35 = np.array([0.092, 0.162, 0.278, 0.318, 0.362, 0.379, 0.395, 0.400, 0.404, 0.411, 0.418, 0.426, 0.433, 0.438, 0.443, 0.450, 0.454])
    il_35 = np.array([8.110, 8.070, 7.770, 7.450, 6.850, 6.420, 5.870, 5.650, 5.450, 5.060, 4.610, 4.110, 3.500, 3.040, 2.520, 1.660, 0.740])

    vl_45 = np.array([0.092, 0.162, 0.289, 0.326, 0.366, 0.380, 0.388, 0.395, 0.403, 0.408, 0.413, 0.419, 0.422, 0.426, 0.430, 0.432])
    il_45 = np.array([8.060, 8.010, 7.510, 7.050, 6.060, 5.440, 5.040, 4.550, 3.990, 3.470, 2.980, 2.440, 2.060, 1.560, 1.070, 0.710])

    vl_55 = np.array([0.09, 0.141, 0.192, 0.239, 0.291, 0.343, 0.369, 0.381, 0.386, 0.391, 0.394, 0.399, 0.403, 0.406, 0.408])
    il_55 = np.array([8.00, 7.960, 7.870, 7.690, 7.220, 6.040, 4.760, 3.870, 3.490, 2.940, 2.570, 1.990, 1.520, 1.010, 0.660])

    vl_65 = np.array([0.098, 0.138, 0.199, 0.230, 0.292, 0.327, 0.358, 0.369, 0.380, 0.384, 0.386])
    il_65 = np.array([8.060, 8.00, 7.840, 7.680, 6.950, 5.920, 4.110, 3.140, 1.720, 1.040, 0.700])

    vl_75 = np.array([0.106, 0.160, 0.198, 0.235, 0.294, 0.317, 0.336, 0.344, 0.349, 0.353, 0.357, 0.359, 0.361])
    il_75 = np.array([7.980, 7.860, 7.700, 7.410, 6.270, 5.210, 3.850, 3.100, 2.330, 1.960, 1.480, 1.010, 0.580])

    plt.title("I-V Characteristics in Light Condition")
    plt.grid(True)
    plt.plot(vl_35, il_35, label=r"$35^{\circ}$C") 
    plt.plot(vl_45, il_45, label=r"$45^{\circ}$C")
    plt.plot(vl_55, il_55, label=r"$55^{\circ}$C")
    plt.plot(vl_65, il_65, label=r"$65^{\circ}$C")
    plt.plot(vl_75, il_75, label=r"$75^{\circ}$C")
    plt.xlabel(r"$V_{d}$ (V)")
    plt.ylabel(r"$I_{d}$ (mA)")
    plt.legend()
    plt.show()

    plt.title("Power Plot in Light Condition")
    plt.grid(True)
    plt.plot(vl_35, vl_35 * il_35, label=r"$35^{\circ}$C") 
    plt.plot(vl_45, vl_45 * il_45, label=r"$45^{\circ}$C")
    plt.plot(vl_55, vl_55 * il_55, label=r"$55^{\circ}$C")
    plt.plot(vl_65, vl_65 * il_65, label=r"$65^{\circ}$C")
    plt.plot(vl_75, vl_75 * il_75, label=r"$75^{\circ}$C")
    plt.xlabel(r"$V_{d}$ (V)")
    plt.ylabel(r"$P_{d}$ (mW)")
    plt.legend()
    plt.show()