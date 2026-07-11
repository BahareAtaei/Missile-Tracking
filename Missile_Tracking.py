"""Missile Tracking"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# print initial information
print('Missile Tracking \n Solve for missing target of slower speed \n Missile launched at (0, 0) toward (0, L) \n Tracks by always aiming at present position of the target \n Missile velocity is q times the target velocity \n Solved analytically')

# get initial input for first problem
L = float(input("Enter x location at y = 0 when target is acquired: "))
q = float(input("Enter speed factor by which missile exceeds target: "))


x = np.linspace(0, L+1e-6, 1000)

# get initial input for second problem
q_values = np.linspace(1.1, 5, 1000)
y_interception = []

# definition of the equation FIGURE1_6
def missile1(x, z):
    y, v = z
    # v = dy/dx
    dydx = v
    dvdx = np.sqrt(1+v**2)/(q*(L-x))
    return [dydx, dvdx]

# definition of the equation FIGURE1_7
def missile2(x, z, q, L):
    y, v = z
    dydx = v
    dvdx = np.sqrt(1+v**2)/(q*L-x)
    return [dydx, dvdx]

# solution of figure1_6
solution1 = solve_ivp(
    missile1,
    [0, L+1e-6], # 0 < x < L
    [0, 0], # y[0]=0, y'[0]=0
    t_eval = x
)

# solution of figure1_7
for i in q_values:
    x2 = np.linspace(0, L+1e-6, 1000)
    solution2 = solve_ivp(
        missile2,
        [0, L+1e-6],
        [0, 0],
        t_eval = x2,
        args=(i, L)
    )

    y_int = solution2.y[0, -1] # y[0][-1] -> interception y
    y_interception.append(y_int/L)

# plotting results
fig, axes = plt.subplots(1, 2, figsize=(12, 8))
fig.suptitle('Missile Tracking', fontsize=30)

# Figure1_6:
axes[0].plot(solution1.t, solution1.y[0], color='green', ls='--', label='Missile Trajectory')
axes[0].axvline(x=L+1e-6, color='red', ls=':', label='Target Line')
axes[0].set_title('Missile and Target', fontsize=15)
axes[0].set_ylabel('y', fontsize=10)
axes[0].set_xlabel('x', fontsize=10)
axes[0].legend(loc='upper left')
axes[0].grid(alpha=0.5, ls='--')

# standard output figure1_6
print('Interception Point is: ', solution1.y[0][-1])

axes[1].plot(q_values, y_interception, color='blue', ls='--', label='Interception y Versus Speed Ratio')
axes[1].set_title('Interception y as a Function of Speed Ratio', fontsize=15)
axes[1].set_ylabel('y_int/L', fontsize=10)
axes[1].set_xlabel('Missile/Target speed ratio', fontsize=10)
axes[1].legend(loc='upper right')
axes[1].grid(alpha=0.5, ls='--')

plt.tight_layout()
plt.show()
