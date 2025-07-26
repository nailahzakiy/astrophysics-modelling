import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Lane-Emden Equation in first-order ODE form
def lane_emden_rhs(xi, y, n):
    theta, phi = y
    if xi == 0:
        dphi_dxi = 0  # Avoid singularity at xi=0
    else:
        dphi_dxi = - (2/xi) * phi - theta**n
    return [phi, dphi_dxi]

# Parameters
n = 3  # Polytropic index, can be changed
xi_max = 20  # Integration limit
y0 = [1, 0]  # Initial conditions: theta(0)=1, theta'(0)=0

# Solve ODE
sol = solve_ivp(lane_emden_rhs, [1e-8, xi_max], y0, args=(n,), dense_output=True, max_step=0.1)

# Extract solution
xi_vals = np.linspace(1e-8, xi_max, 1000)
theta_vals = sol.sol(xi_vals)[0]

# Find the first zero crossing (theta = 0), which defines stellar surface
surface_index = np.where(theta_vals <= 0)[0]
xi_surface = xi_vals[surface_index[0]] if surface_index.size > 0 else None

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(xi_vals, theta_vals, label=f"n = {n}")
if xi_surface:
    plt.axvline(x=xi_surface, color='r', linestyle='--', label=f"Surface: ξ ≈ {xi_surface:.2f}")
plt.title("Solution of Lane-Emden Equation")
plt.xlabel("ξ (dimensionless radius)")
plt.ylabel("θ (dimensionless density)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
