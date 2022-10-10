import numpy as np
import matplotlib.pyplot as plt

intensity = np.array([1000, 1500, 2000])

i_red = np.array([2, 3, 4])
vout_red = np.array([4.09, 5.32, 6.59])

i_blue = np.array([0.303, 0.417, 0.579])
vout_blue = np.array([2.70, 3.04, 3.15])

i_ir = np.array([4.51, 5.17, 6.28])
vout_ir = np.array([4.04, 4.36, 4.85])

plt.plot(intensity, vout_ir, label="IR LED", color="green")
plt.plot(intensity, vout_red, label="Red LED", color="red")
plt.plot(intensity, vout_blue, label="Blue LED", color="blue")
plt.title(r"$V_{out}$ vs Intensity for Photodiode")
plt.xlabel("Intensity (lux)")
plt.ylabel(r"$V_{out}$ (V)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

wavelength = np.array([950, 750, 450])

vout_1000 = np.array([4.04, 4.09, 2.70])
vout_1500 = np.array([4.36, 5.32, 3.04])
vout_2000 = np.array([4.85, 6.59, 3.15])

plt.plot(wavelength, vout_1000, label="1000 lux")
plt.plot(wavelength, vout_1500, label="1500 lux")
plt.plot(wavelength, vout_2000, label="2000 lux")
plt.title(r"$V_{out}$ vs Wavelength for Photodiode")
plt.xlabel("Wavelength (nm)")
plt.ylabel(r"$V_{out}$ (V)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
