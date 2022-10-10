import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    vcb_1 = np.array([0.649, 0.631, 0.534, 0.501, 0.462, 0.372, 0.300, 0.257, 0.109, 0.048, -0.001, -0.048, -0.103, -0.207, -0.305, -0.490, -0.999, -1.516])*(-1)
    ic_1 =  np.array([0.760, 0.890, 0.980, 0.985, 0.990, 0.995, 1.000, 1.010, 1.010, 1.010, 1.0100, 1.0100, 1.0100, 1.0100, 1.0100, 1.0100, 1.0100, 1.0100])

    vcb_4 = np.array([0.732, 0.710, 0.694, 0.606, 0.487, 0.450, 0.447, 0.404, 0.307, 0.128, -0.015, -0.505, -0.963, -1.432])*(-1)
    ic_4 =  np.array([1.684, 2.630, 3.140, 3.920, 3.930, 3.940, 3.945, 3.950, 3.950, 3.950, 3.9500, 3.9500, 3.9550, 3.9600])

    vcb_7 = np.array([0.753, 0.746, 0.743, 0.739, 0.731, 0.722, 0.716, 0.695, 0.661, 0.614, 0.539, 0.428, 0.407, 0.374, 0.110, -0.026, -0.465, -0.984, -1.407])*(-1)
    ic_7 =  np.array([2.730, 3.440, 3.670, 4.060, 4.570, 5.100, 5.280, 5.995, 6.470, 6.780, 6.890, 6.930, 6.940, 6.950, 6.950, 6.9500, 6.9500, 6.9550, 6.960])

    vcb_10 = np.array([0.766, 0.765, 0.761, 0.758, 0.754, 0.750, 0.746, 0.736, 0.723, 0.717, 0.703, 0.692, 0.678, 0.591, 0.557, 0.295, 0.116, 0.050, -0.002, -0.489, -0.997, -1.491])*(-1)
    ic_10 =  np.array([3.670, 3.970, 4.520, 4.910, 5.350, 5.790, 6.190, 7.010, 7.860, 8.180, 8.680, 8.950, 9.210, 9.770, 9.790, 9.810, 9.830, 9.890, 9.8950, 9.9000, 9.9100, 9.9100])

    plt.title("Output Characteristics of BJT in CB Configuration")
    plt.plot(vcb_1, ic_1, label=r"$I_{E}=1mA$")
    plt.plot(vcb_4, ic_4, label=r"$I_{E}=4mA$")
    plt.plot(vcb_7, ic_7, label=r"$I_{E}=7mA$")
    plt.plot(vcb_10, ic_10, label=r"$I_{E}=10mA$")
    plt.xlabel(r"$V_{CB}$")
    plt.ylabel(r"$I_{C}$")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()