import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    vbe = np.array([0.55, 0.57, 0.59, 0.60, 0.62, 0.63, 0.64, 0.65, 0.66, 0.670, 0.690, 0.700, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77])
    ic  = np.array([0.10, 0.20, 0.64, 0.93, 1.73, 2.39, 3.24, 5.25, 5.46, 5.730, 6.020, 6.110, 6.29, 6.54, 6.91, 7.25, 8.14, 8.83, 9.32])
    ib  = np.array([0.50, 1.00, 3.10, 4.40, 8.30, 11.4, 15.3, 26.3, 58.5, 195.5, 898.0, 1068, 1366, 1794, 2870, 3580, 5430, 6880, 7940])/1000

    plt.title("Gummel Plot")
    plt.plot(np.log(ic), ic / ib)
    plt.xlabel(r"$\ln{I_{C}}$")
    plt.ylabel(r"$\beta_{dc}$")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

    plt.title(r"$I_{C}$, $I_{B}$ vs $V_{BE}$")
    plt.plot(vbe, np.log(ic), label=r"$I_{C}$")
    plt.plot(vbe, np.log(ib), label=r"$I_{B}$")
    plt.xlabel(r"$V_{BE}$")
    plt.ylabel(r"$I$")
    plt.yscale("log")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

    plt.title(r"$\beta_{dc}$ vs $V_{BE}$")
    plt.plot(vbe, np.log(ic / ib))
    plt.xlabel(r"$V_{BE}$")
    plt.ylabel(r"$\ln{\beta_{dc}}$")
    plt.yscale("log")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
