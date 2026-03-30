import math
import numpy as np
import matplotlib.pyplot as plt

#Day 4,5 - Matplotlib Visualisation & Weak Acid + Buffer Logic Implementation
def pH_calculator(v_acid, c_acid, c_base, yes_or_no, ka):

    eq_point = (v_acid) * c_acid / c_base   #in cm^3

    v_base = np.linspace(0, eq_point *2, 1000)  #in cm^3
    safe_v_base = np.where(v_base == 0, 1e-5, v_base)

    moles_acid_initial = v_acid * c_acid / 1000
    moles_base_added = v_base * c_base / 1000
    net_moles = moles_acid_initial - moles_base_added

    pka = -np.log10(ka)
    c_salt = moles_acid_initial / (eq_point + v_acid) * 1000    #at equivalence point

    acid_mask = (v_base > 0) & (v_base < eq_point - 0.1)
    base_mask = v_base > eq_point + 0.1

    v_total = v_acid + v_base   #in cm^3
    conc_h = np.maximum(np.abs(net_moles / v_total * 1000), 1e-15)
    with np.errstate(divide='ignore'):  #avoid calculation error at the equivalence point
            if yes_or_no == "Y":
                pH_eq = 7
                pH_values = np.where(v_base == 0, -np.log10(np.maximum(c_acid, 1e-15)),
                            np.where(acid_mask, -np.log10(conc_h),
                            np.where(base_mask, 14 + np.log10(conc_h),
                                    7.00)))

            elif yes_or_no == "N":
                pH_eq = 7 + 0.5 * (pka + np.log10(c_salt))  #weak base salt formula
                
                pH_initial = -0.5 * np.log10(np.maximum(ka * c_acid, 1e-15))
                pH_buffer = pka + np.log10(np.maximum(moles_base_added / net_moles, 1e-15))   #Henderson-Hasselbalch formula
            
                pH_values = np.where(v_base == 0, pH_initial,
                            np.where(acid_mask, pH_buffer,
                            np.where(base_mask, 14 + np.log10(conc_h),
                                    pH_eq)))
                
            return v_base, pH_values, eq_point, pH_eq


while  True:
    strong_acid = str((input("Is the a Strong Acid (Y/N)? ")))

    if strong_acid == "Y":
        get_ka = 0
        break   #to exit this 'safety net'
    elif strong_acid == "N":
        get_ka = float(input("Acid Dissociation Constant: "))
        break
    else:
        print("Invalid Input! Enter Y or N.")

get_v_acid = float(input("Volume of the Monoprotic Acid (cm^3): "))
get_c_acid = float(input("Concentration of the Monoprotic Acid (dm^-3): "))
get_c_base = float(input("Concentration of a Strong Monoprotic Base (dm^-3): "))

output_base, output_pH , output_eq_volume, output_pH_eq = pH_calculator(get_v_acid, get_c_acid, get_c_base, strong_acid, get_ka)

#Ploting the results
plt.figure(figsize=(8,6))   #creating the figure
plt.plot(output_base, output_pH, color="royalblue", linewidth=2, label="Titration Curve")

if strong_acid == "Y":
    x = "Strong"
else:
    x = "Weak"

plt.title(f"Titrating a {x} Acid ({get_v_acid:.2f} cm³, {get_c_acid:.2f} moldm⁻³) againist a Strong Base ({get_c_base:.2f} moldm⁻³)")
plt.xlabel(r"Volume of Strong Base Added (cm$^3$)") #alternative method to display the cube
plt.ylabel("pH")

plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=output_pH_eq, color="red", linestyle=":", label=f"Equivalence Point pH={output_pH_eq:.2f}")
plt.axvline(x=output_eq_volume, color="green", linestyle=":", label="Equivalence Point Volume")

tick_spacing = max(5, round((output_eq_volume * 2) / 50) * 5)  #added this to ensure proper ticking on the x-axis (even if the volume of base gets really large)

plt.xticks(np.arange(0, (output_eq_volume * 2) + 1, tick_spacing))
plt.yticks(np.arange(0, 15, 1)) #y-axis ticks every 1pH unit

#Plotting the half-equivalence point
if strong_acid == "N":
    half_eq_vol = output_eq_volume / 2
    pka_val = -math.log10(get_ka)
    
    plt.scatter(half_eq_vol, pka_val, color='orange', zorder=5) #a point instead of a line
    plt.annotate(f"Half-Eq: pH = pKa = {pka_val:.2f}", (half_eq_vol, pka_val), textcoords="offset points", xytext=(10,-10), ha='left', fontsize=9, color='darkorange', fontweight='bold')

#Created a text box to display the pH and the volume of base added at the equivalence point
stats_text = f"Equivalence Point:\n Vol: {output_eq_volume:.2f} cm³ \n pH: {output_pH_eq:.2f}"

plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
#Placing this text box on the top left, and keeps it in the corner regardless of zoom

plt.legend()
plt.show()