import numpy as np

# =======================
# Settings
# =======================
# Path to your data file
filename = "data.dat"   # change this to your file name

# Column indices (0-based):
# col_strain: which column has strain (Δa/a0)
# col_energy: which column has band edge energy (eV)
col_strain = 0
col_energy = 1

# =======================
# Load data
# =======================
# Assumes:
# - whitespace-separated columns
# - may have comments starting with '#'
data = np.loadtxt(filename, comments='#')

strain = data[:, col_strain]
E_edge = data[:, col_energy]

# =======================
# Linear fit: E_edge(ε) ≈ E0 + E1 * ε
# =======================
# polyfit returns [slope, intercept] for degree=1
E1, E0 = np.polyfit(strain, E_edge, 1)

print("===== Deformation potential fitting =====")
print("Fitted equation: E_edge(ε) ≈ E0 + E1 * ε")
print(f"E0 (E_edge at zero strain) = {E0:.6f} eV")
print(f"E1 (deformation potential) = {E1:.6f} eV")  # THIS is what you want

