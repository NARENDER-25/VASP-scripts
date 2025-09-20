{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQVsiISDH/Ml4NQf4cDIdd"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Bx3qMlNvxSyc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6afe62e7-e3b0-4293-c39e-7d55456cb875"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the value of m_e: 0.4\n",
            "Enter the value of m_h: 0.8\n",
            "Enter the value of epsilon_in_plane: 12\n",
            "Enter the value of epsilon_out_of_plane: 01\n",
            "Effective exciton mass (μ_ex): 0.267 m0\n",
            "Average static dielectric constant (ε_avg): 6.500\n",
            "Exciton binding energy (E_exb): 0.086 eV\n"
          ]
        }
      ],
      "source": [
        "# ------------------------------------------------------#\n",
        "# Exciton Binding Energy Calculator                     #\n",
        "# Author: Narender Kumar                                #\n",
        "# United Arab Emirates University, Abu Dhabi UAE        #\n",
        "#-------------------------------------------------------#\n",
        "# This script calculates the effective mass             #\n",
        "# average dielectric constant, and exciton binding      #\n",
        "# energy based on user input.                           #\n",
        "#-------------------------------------------------------#\n",
        "# Please refer the following paper for details          #\n",
        "# ACS Omega 2021 6 (17), 11545-11555                    #\n",
        "# DOI: 10.1021/acsomega.1c00734                         #\n",
        "#########################################################\n",
        "\n",
        "import math\n",
        "m_e = float(input(\"Enter the value of m_e: \"))\n",
        "m_h = float(input(\"Enter the value of m_h: \"))\n",
        "m0 = 9.10938356e-31\n",
        "mu = (m_e * m_h)/(m_e + m_h)\n",
        "epsilon_in_plane = float(input(\"Enter the value of epsilon_in_plane: \"))\n",
        "epsilon_out_of_plane = float(input(\"Enter the value of epsilon_out_of_plane: \"))\n",
        "epsilon_avg =  (epsilon_in_plane + epsilon_out_of_plane) / 2\n",
        "\n",
        "E_exb = (13.6057 * mu)/(epsilon_avg**2)\n",
        "\n",
        "print(f\"Effective exciton mass (μ_ex): {mu:.3f} m0\")\n",
        "print(f\"Average static dielectric constant (ε_avg): {epsilon_avg:.3f}\")\n",
        "print(f\"Exciton binding energy (E_exb): {E_exb:.3f} eV\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "0"
      ],
      "metadata": {
        "id": "mK6sEbiH1sbM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "27b36836-8692-49bb-8346-1215c33a9d63"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    }
  ]
}