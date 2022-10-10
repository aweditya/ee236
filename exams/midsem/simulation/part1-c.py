import numpy as np
import matplotlib.pyplot as plt

temp = np.array([25,35,45,55,65,75])
ir = np.array([-1.601737e-03, -1.615689e-03, -1.650096e-03, -1.730376e-03, -1.908469e-03, -2.285766e-03])

plt.plot(temp, ir)
plt.title("Part 1c iii")
plt.xlabel(r"Temperature ($^{\circ}$C)")
plt.ylabel("Reverse Current at -1.5V (A)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.show()

ill = np.array([0.5, 1, 1.5, 2, 2.5, 3])
il = np.array([-1.103729e-03, -1.601737e-03, -2.099745e-03, -2.597753e-03, -3.095761e-03, -3.593769e-03])

plt.plot(ill, il)
plt.title("Part 1c iv")
plt.xlabel("Illumination (mA)")
plt.ylabel("Reverse Current at -1.5V (A)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.show()
