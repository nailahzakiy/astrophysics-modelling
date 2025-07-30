import numpy as np
import matplotlib.pyplot as plt

# Parameter
n = 1.5
h = 0.01
xi_max = 10
epsilon = 1e-5

# Fungsi sistem ODE Lane-Emden
def f(xi, y1, y2):
    dy1dxi = y2
    if xi == 0 or y1 < 0:
        dy2dxi = 0
    else:
        dy2dxi = - (2/xi)*y2 - y1**n
    return dy1dxi, dy2dxi

# Inisialisasi
xi_values = [epsilon]
y1_values = [1 - (1/6)*epsilon**2]
y2_values = [- (1/3)*epsilon]

# RK4 Loop
xi = epsilon
while xi < xi_max and y1_values[-1] > 0:
    y1, y2 = y1_values[-1], y2_values[-1]
    
    k1_1, k1_2 = f(xi, y1, y2)
    k2_1, k2_2 = f(xi + h/2, y1 + h*k1_1/2, y2 + h*k1_2/2)
    k3_1, k3_2 = f(xi + h/2, y1 + h*k2_1/2, y2 + h*k2_2/2)
    k4_1, k4_2 = f(xi + h, y1 + h*k3_1, y2 + h*k3_2)

    y1_new = y1 + h*(k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6
    y2_new = y2 + h*(k1_2 + 2*k2_2 + 2*k3_2 + k4_2)/6
    
    if isinstance(y1_new, complex):
        break

    xi += h
    xi_values.append(xi)
    y1_values.append(y1_new)
    y2_values.append(y2_new)

for i in range(1, len(y1_values)):
    if y1_values[i] <= 0:
        xi_zero = xi_values[i-1] + (0 - y1_values[i-1]) * (xi_values[i] - xi_values[i-1]) / (y1_values[i] - y1_values[i-1])
        break
print(f"xi saat theta = 0: {xi_zero}")

# Plot hasil
plt.plot(xi_values, y1_values, label=r'$\theta(\xi)$')
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\theta$')
plt.title('Lane-Emden Numerical Solution (n=1.5)')
plt.grid()
plt.legend()
plt.show()