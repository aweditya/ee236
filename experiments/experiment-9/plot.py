import matplotlib.pyplot as plt 
import numpy as np

if __name__ == "__main__":
    vt = 1.27

    # 50 degrees
    vgs_50 = np.array([1.58, 1.60, 1.72, 1.95, 2.06, 2.17, 2.39, 2.77, 3.08, 3.21, 3.43, 3.67, 3.94, 5.01, 6.03, 7.04, 8.05, 9.30, 9.98])
    id_50  = np.array([23.0, 27.0, 54.0, 132., 163., 186., 214., 237., 245., 248., 253., 258., 262., 273., 279., 285., 288., 291., 293.])
    beta_50 = 2 * (np.sqrt(id_50) / (vgs_50 - vt)) ** 2

    # 70 degrees
    vgs_70  = np.array([1.52, 1.61, 1.72, 1.79, 1.96, 2.03, 2.05, 2.22, 2.45, 2.91, 3.31, 3.78, 4.06, 5.16, 6.11, 7.00, 8.08, 9.08, 10.14])
    id_70   = np.array([18.0, 33.0, 60.0, 80.0, 137., 156., 162., 190., 216., 235., 246., 255., 258., 269., 276., 280., 284., 287., 290.0])
    beta_70 = 2 * (np.sqrt(id_70) / (vgs_70 - vt)) ** 2

    # 35 degrees
    vgs_35  = np.array([1.57, 1.86, 2.23, 2.51, 2.85, 3.05, 3.61, 3.97, 4.31, 5.17, 5.95, 6.75, 7.31, 8.48, 9.26, 9.92])
    id_35   = np.array([30.0, 113., 202., 233., 252., 262., 279., 286., 290., 299., 305., 307., 308., 313., 314., 314.])
    beta_35 = 2 * (np.sqrt(id_35) / (vgs_35 - vt)) ** 2

    plt.title(r"$I_{D}$ vs $V_{GS}$")
    plt.plot(vgs_35, id_35, label=r"35$^{\circ}$C")
    plt.plot(vgs_50, id_50, label=r"50$^{\circ}$C")
    plt.plot(vgs_70, id_70, label=r"70$^{\circ}$C")
    plt.xlabel(r"$V_{GS}$ (V)")
    plt.ylabel(r"$I_{D}$ (mA)")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.title(r"$\beta$ vs $V_{GS}$")
    plt.plot(vgs_35, beta_35, label=r"35$^{\circ}$C")
    plt.plot(vgs_70, beta_70, label=r"50$^{\circ}$C")
    plt.plot(vgs_50, beta_50, label=r"70$^{\circ}$C")
    plt.xlabel(r"$V_{GS}$")
    plt.ylabel(r"${\beta} ~mA/V^{2}$")
    plt.grid(True)
    plt.legend()
    plt.show()
