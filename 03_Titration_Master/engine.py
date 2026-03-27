import math
import numpy as np

#Day 2,3 - Vectorised Ttration Engine with NumPy
def pH_calculator(v_acid, c_acid, c_base):

    eq_point = (v_acid) * c_acid / c_base   #in cm^3

    v_base = np.linspace(0, eq_point *2, 1000)  #in cm^3
    net_moles = v_acid / 1000 * c_acid - v_base / 1000 * c_base
    acid_mask = net_moles > 0
    base_mask = net_moles < 0

    v_total = v_acid + v_base   #in cm^3
    conc_h = np.abs(net_moles / v_total * 1000)
    with np.errstate(divide='ignore'):  #avoid calculation error at the equivalence point
        pH_values = np.where(acid_mask, - np.log10 (conc_h), np.where(base_mask, 14 + np.log10 (conc_h), 7.00))
    return v_base, pH_values

get_v_acid = float(input("Volume of a Strong Monoprotic Acid (cm^3): "))
get_c_acid = float(input("Concentration of a Strong Monoprotic Acid (dm^-3): "))
get_c_base = float(input("Concentration of a Strong Monoprotic Base (dm^-3): "))

output_base, output_pH = pH_calculator(get_v_acid, get_c_acid, get_c_base)

print(f"Initial pH: {output_pH[0:5]}")
print(f"Final pH: {output_pH[-5:]}")