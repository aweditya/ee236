import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Order - Si, Red, Green, Blue, White
    cut_in = [0.75, 1.90, 2.70, 2.71, 2.80]
    band_gap = [1.1, 1.984, 2.384, 2.725, 2.755]

    plt.plot(band_gap, cut_in)

    plt.title('Variation of Cut-in Voltage with Bandgap Energy')
    plt.xlabel('Bandgap (eV)')
    plt.ylabel('Cut-in Voltage (V)')
    
    plt.show()
