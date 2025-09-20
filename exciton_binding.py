#########################################################
# Exciton Binding Energy Calculator                     #
# Author: Narender Kumar                                #
# United Arab Emirates University, Abu Dhabi UAE        #
#-------------------------------------------------------#
# This script calculates the effective mass             #
# average dielectric constant, and exciton binding      #
# energy based on user input.                           #
#-------------------------------------------------------#
# Please refer the following paper for details          #
# ACS Omega 2021 6 (17), 11545-11555                    #
# DOI: 10.1021/acsomega.1c00734                         #
#########################################################

import math
m_e = float(input("Enter the value of m_e: "))
m_h = float(input("Enter the value of m_h: "))
m0 = 9.10938356e-31
mu = (m_e * m_h)/(m_e + m_h)
epsilon_in_plane = float(input("Enter the value of epsilon_in_plane: "))
epsilon_out_of_plane = float(input("Enter the value of epsilon_out_of_plane: "))
epsilon_avg =  (epsilon_in_plane + epsilon_out_of_plane) / 2

E_exb = (13.6057 * mu)/(epsilon_avg**2)

print(f"Effective exciton mass (μ_ex): {mu:.3f} m0")
print(f"Average static dielectric constant (ε_avg): {epsilon_avg:.3f}")
print(f"Exciton binding energy (E_exb): {E_exb:.3f} eV")
