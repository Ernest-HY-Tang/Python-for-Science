import math
import numpy as np
import matplotlib.pyplot as plt

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
    return v_base, pH_values, eq_point

#get_v_acid = float(input("Volume of a Strong Monoprotic Acid (cm^3): "))
#get_c_acid = float(input("Concentration of a Strong Monoprotic Acid (dm^-3): "))
#get_c_base = float(input("Concentration of a Strong Monoprotic Base (dm^-3): "))

get_v_acid = 25
get_c_acid = 0.1
get_c_base = 0.1

output_base, output_pH , output_eq_volume = pH_calculator(get_v_acid, get_c_acid, get_c_base)

#Ploting the results
plt.figure(figsize=(8,6))   #creating the figure
plt.plot(output_base, output_pH, color='royalblue', linewidth=2, label='Titration Curve')

plt.title(f"Titrating a Strong Acid ({get_v_acid} cm^3, {get_c_acid} moldm^-3) againist a Strong Base ({get_c_base} mol dm^-3)")
plt.xlabel("Volume of Strong Base Added (cm^3)")
plt.ylabel("pH")

plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=7, color='red', linestyle=':', label='Equivalence Point pH=7')
plt.axvline(x=output_eq_volume, color='green', linestyle=':', label='Equivalence Point Volume')


plt.xticks(np.arange(0, (output_eq_volume * 2) + 1, 5)) #set x-axis ticks every (5cm^3) and ensures the final point is labelled
plt.yticks(np.arange(0, 15, 1)) #y-axis ticks every 1pH unit

# Create the text string (f-string for easy variables)
stats_text = f'Equivalence Point:\nVol: {output_eq_volume:.2f} cm³\npH: 7.00'

plt.text(0.05, 0.95, stats_text,
         transform=plt.gca().transAxes,
         fontsize=10, 
         verticalalignment='top', 
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)) #placing this text box on the top left, and keeps it in the corner regardless of zoom

plt.legend()
plt.show()