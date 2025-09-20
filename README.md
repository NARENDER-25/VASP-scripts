#  delete_vasp_large_files.sh
A **safe and interactive Bash script** to delete multiple file patterns across various directories and/or subdirectories.

> ⚠️ Use with caution. This script **permanently deletes files** after your confirmation.

---

## 🛠️ Features

- Accepts **multiple directories** as input
- Accepts **multiple file name patterns** (e.g., `CHG*`, `*.xml`, `OUTCAR`)
- Option to **include or exclude subdirectories**
- Shows **directory size** and **top 5 largest files** before deletion
- Lists **all files that match your patterns** before asking for final confirmation
- Requires **a single final confirmation** (`delete`) to proceed
- Measures and displays **execution time**

---

## 📋 How It Works

1. Prompts you for directories
2. Verifies the directories exist
3. Shows a summary of disk usage and the largest files
4. Prompts you for file name patterns to delete
5. Optionally includes subdirectories
6. Displays all matching files
7. Prompts for a **final, one-word confirmation**
8. Deletes the listed files

---

## Getting Started

### 1. Clone the repository or download the script

```bash
bash delete_vasp_large_files.sh
