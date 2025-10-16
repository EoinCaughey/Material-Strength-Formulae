# Material Strength Engineering Calculators

This repository contains a set of small **Python scripts** that perform essential **structural and mechanical engineering calculations**, including:

- **Euler Buckling Limit** for slender columns  
- **Maximum Stress and Internal Pressure** in **steel cylinders**

These tools were designed for me during my time studying material strength in order to solve problems quickly.

---

## Project Overview

### 1. `euler_buckling.py`
This script calculates the **critical buckling load** of a column using **Euler’s Buckling Formula**.

#### Formula

\[
P_{cr} = \frac{\pi^2 E I}{(K L)^2}
\]

Where:  
- \( P_{cr} \): Critical buckling load (N)  
- \( E \): Young’s modulus (Pa)  
- \( I \): Area moment of inertia (m⁴)  
- \( K \): Effective length factor (dimensionless, depends on boundary conditions)  
- \( L \): Length of the column (m)

## 2. `steel_cylinder.py`
This script calculates the maximum hoop stress in a **thin-walled cylinder**.

For a **thin-walled cylinder** (wall thickness much smaller than radius), the hoop stress is:

\[
\sigma_h = \frac{p \, r_i}{t}
\]

Where:  
- \( \sigma_h \) : Hoop (circumferential) stress (Pa)  
- \( p \) : Internal pressure (Pa)  
- \( r_i \) : Inner radius (m)  
- \( t \) : Wall thickness (m)
