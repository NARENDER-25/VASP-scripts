#  delete_vasp_large_files.sh
A **safe and interactive Bash script** to delete multiple file patterns across various directories and/or subdirectories.

## 🛠️ Features

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
bash delete_vasp_large_files.sh
> ⚠️ Use with caution. This script **permanently deletes files** after your confirmation.
