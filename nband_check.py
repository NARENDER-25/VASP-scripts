#!/usr/bin/env python3
# check_nbands.py

import subprocess

# From OUTCAR
try:
    result = subprocess.run(['grep', 'NBANDS', 'OUTCAR'],
                           capture_output=True, text=True)
    print("=== From OUTCAR ===")
    print(result.stdout[:500])
except:
    pass

# From EIGENVAL
try:
    with open('EIGENVAL') as f:
        lines = f.readlines()
    nbands = int(lines[5].split()[2])
    nkpts  = int(lines[5].split()[1])
    nelect = int(lines[0].split()[0])
    print(f"\n=== From EIGENVAL ===")
    print(f"NBANDS = {nbands}")
    print(f"NKPTS  = {nkpts}")
    print(f"NELECT ~ {nelect}")
except:
    pass

# Manual estimate
try:
    with open('OUTCAR') as f:
        for line in f:
            if 'NELECT' in line:
                nelect = float(line.split()[2])
                break
    with open('POSCAR') as f:
        poscar = f.readlines()
    nions = sum(int(x) for x in poscar[6].split())
    
    nbands_default = max(int(nelect/2) + int(nions/2),
                        int(nelect * 0.6))
    
    # For NAMD: recommended = default + extra empty bands
    nbands_namd = nbands_default + 20  # ~20 extra empty bands above CBM
    
    print(f"\n=== Manual Estimate ===")
    print(f"NELECT         = {int(nelect)}")
    print(f"NIONS          = {nions}")
    print(f"Default NBANDS = {nbands_default}")
    print(f"Recommended for NAMD (CBM study)  = {nbands_default + 10}")
    print(f"Recommended for NAMD (hot carrier) = {nbands_default + 20}")
except Exception as e:
    print(f"Error: {e}")
