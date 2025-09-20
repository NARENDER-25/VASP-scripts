## 1.  delete_vasp_large_files.sh
A **safe and interactive Bash script** to delete multiple file patterns across various directories and/or subdirectories.

## Features
- Accepts **multiple directories** as input
- Accepts **multiple file name patterns** (e.g., `CHG*`, `*.xml`, `OUTCAR`)
- Option to **include or exclude subdirectories**
- Shows **directory size** and **top 5 largest files** before deletion
- Lists **all files that match your patterns** before asking for final confirmation
- Requires **a single final confirmation** (`delete`) to proceed
- Measures and displays **execution time**

## Getting Started

### 1. Clone the repository or download the script

```bash
bash delete_vasp_files.sh
> ⚠️ Use with caution. This script **permanently deletes files** after your confirmation.

---

## 2. Exciton Binding Energy Calculator

This script calculates the **exciton binding energy (E<sub>exb</sub>)**:
### What It Does
The script prompts the user to input:
- Electron effective mass (*mₑ*) in units of m₀  
- Hole effective mass (*mₕ*) in units of m₀  
- In-plane dielectric constant (*ε<sub>in</sub>*)  
- Out-of-plane dielectric constant (*ε<sub>out</sub>*)
It then calculates:
- Reduced exciton mass:  
  \[
  \mu = \frac{m_e \cdot m_h}{m_e + m_h}
  \]
- Average dielectric constant:  
  \[
  \epsilon_{\text{avg}} = \frac{\epsilon_{\text{in}} + \epsilon_{\text{out}}}{2}
  \]
- Exciton binding energy using the hydrogenic model:  
  \[
  E_{\text{exb}} = \frac{13.6057 \cdot \mu}{\epsilon_{\text{avg}}^2}
  \]

### Usage
Run the script in any Python 3 environment:

```bash
python exciton_binding_energy.py
###  Reference
This script is based on the model and methodology described in:
> **ACS Omega 2021, 6 (17), 11545–11555**  
> [DOI: 10.1021/acsomega.1c00734](https://doi.org/10.1021/acsomega.1c00734)



