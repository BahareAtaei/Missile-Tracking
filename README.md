# Missile-Tracking

Python implementation inspired by the concepts presented in
"More Physics with MATLAB" by Dan Green.

This repository contains my own implementations for learning purposes.

---

**Program Summary:**

This program simulates a **missile pursuit problem** where a missile tracks a moving target using a **pure pursuit guidance law** (always aiming directly at the target's current position).

**Scenario:**
- Missile launched from `(0, 0)` 
- Target moves along the vertical line `x = L` (from `y = 0` upward)
- Missile speed is `q` times faster than the target (`q > 1`)

**Physics/Math:**
The missile's trajectory is governed by a differential equation derived from the pursuit geometry:
```
dy/dx = v
dv/dx = sqrt(1+v^2) / (q·(L-x))
```
where `v = dy/dx` is the slope of the missile's path.

**What the program does:**

1. **Takes user inputs:**
   - `L`: target's x-position (acquisition distance)
   - `q`: speed ratio (missile speed / target speed)

2. **Solves two problems numerically** using `scipy.integrate.solve_ivp`:

   - **Problem 1 (Figure 1.6):** Simulates a single missile trajectory with user-specified `q` and `L`, showing the interception point
   
   - **Problem 2 (Figure 1.7):** Computes interception points for a range of `q` values (from 1.1 to 5) to show how interception location varies with speed ratio

3. **Visualizes results** in two side-by-side plots:
   - **Left plot:** Missile trajectory curve showing the pursuit path to interception
   - **Right plot:** Normalized interception position (`y_int/L`) vs. speed ratio (`q`), showing that higher speed ratios lead to interception closer to the launch point

**Key output:** The interception point where the missile catches the target on the vertical line `x = L`.

---

**In one sentence:** *A numerical simulation of a pure pursuit missile tracking problem that calculates and visualizes interception points for different missile-to-target speed ratios.*
