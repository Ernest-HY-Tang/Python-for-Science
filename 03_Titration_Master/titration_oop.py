import numpy as np
import matplotlib.pyplot as plt

class Acid:
    def __init__(self, name, vol, conc, ka=None):    #ka requires a default 'None'
        self.name = name
        self.vol = vol
        self.conc = conc
        self.ka = ka
    
    def pH_calculator(self):        #small method to calculate initial pH
        if self.ka is not None:
            return -0.5*np.log10(self.ka*self.conc)
        else:
            return -np.log10(self.conc)
        
class Base:
    def __init__(self, name, conc):
        self.name = name
        self.conc = conc

    def moles_base_added(self, v_base):     #small method to calculate the moles of base added
        return self.conc * v_base / 1000


class ActualTitration:
    def __init__(self, acid, base):
        self.acid = acid
        self.base = base

    def generating_curve(self, max_v_base = 100):
        eq_point = (self.acid.vol) * self.acid.conc / self.base.conc  

        v_base = np.linspace(0, eq_point *2, max_v_base)  #in cm^3

        moles_acid_initial = self.acid.vol * self.acid.conc / 1000
        moles_base_added = v_base * self.base.conc / 1000
        net_moles = moles_acid_initial - moles_base_added

    
        c_salt = moles_acid_initial / (eq_point + self.acid.vol) * 1000    #at equivalence point

        acid_mask = (v_base > 0) & (v_base < eq_point)
        base_mask = v_base > eq_point

        v_total = self.acid.vol + v_base   #in cm^3
        conc_h = np.maximum(np.abs(net_moles / v_total * 1000), 1e-15)
        with np.errstate(divide='ignore'):  #avoid calculation error at the equivalence point
            if self.acid.ka is None:
                pH_eq = 7
                pH_values = np.where(v_base == 0, -np.log10(np.maximum(self.acid.conc, 1e-15)),
                            np.where(acid_mask, -np.log10(conc_h),
                            np.where(base_mask, 14 + np.log10(conc_h),
                                    7.00)))

            elif self.acid.ka is not None:
                pka = -np.log10(self.acid.ka)
                pH_eq = 7 + 0.5 * (pka + np.log10(c_salt))  #weak base salt formula
                
                pH_initial = -0.5 * np.log10(np.maximum(self.acid.ka * self.acid.conc, 1e-15))
                pH_buffer = pka + np.log10(np.maximum(moles_base_added / net_moles, 1e-15))   #Henderson-Hasselbalch formula
                pH_buffer = np.maximum(pH_buffer, pH_initial)

                pH_values = np.where(v_base == 0, pH_initial,
                            np.where(acid_mask, pH_buffer,
                            np.where(base_mask, 14 + np.log10(conc_h),
                                    pH_eq)))
                
            return v_base, pH_values, eq_point, pH_eq

    def plotting(self, output_base, output_pH, output_eq_volume, output_pH_eq):
        #Ploting the results
        plt.figure(figsize=(8,6))   #creating the figure
        plt.plot(output_base, output_pH, color="royalblue", linewidth=2, label="Titration Curve")

        if self.acid.ka is None:
            x = "Strong"
        else:
            x = "Weak"

        plt.title(f"Titrating a {x} Acid ({self.acid.vol:.2f} cm³, {self.acid.conc:.2f} moldm⁻³) againist a Strong Base ({self.base.conc:.2f} moldm⁻³)")
        plt.xlabel(r"Volume of Strong Base Added (cm$^3$)") #alternative method to display the cube
        plt.ylabel("pH")

        plt.grid(True, linestyle="--", alpha=0.6)
        plt.axhline(y=output_pH_eq, color="red", linestyle=":", label=f"Equivalence Point pH={output_pH_eq:.2f}")
        plt.axvline(x=output_eq_volume, color="green", linestyle=":", label="Equivalence Point Volume")

        tick_spacing = max(5, round((output_eq_volume * 2) / 50) * 5)  #added this to ensure proper ticking on the x-axis (even if the volume of base gets really large)

        plt.xticks(np.arange(0, (output_eq_volume * 2) + 1, tick_spacing))
        plt.yticks(np.arange(0, 15, 1)) #y-axis ticks every 1pH unit

        #Plotting the half-equivalence point
        if self.acid.ka is not None:
            half_eq_vol = output_eq_volume / 2
            pka_val = -np.log10(self.acid.ka)
    
            plt.scatter(half_eq_vol, pka_val, color='orange', zorder=5) #a point instead of a line
            plt.annotate(f"Half-Eq: pH = pKa = {pka_val:.2f}", (half_eq_vol, pka_val), textcoords="offset points", xytext=(10,-10), ha='left', fontsize=9, color='darkorange', fontweight='bold')

        #Created a text box to display the pH and the volume of base added at the equivalence point
        stats_text = f"Equivalence Point:\n Vol: {output_eq_volume:.2f} cm³ \n pH: {output_pH_eq:.2f}"

        plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
        #Placing this text box on the top left, and keeps it in the corner regardless of zoom

        plt.legend()
        plt.show()
        
        
#For testing:
HCl = Acid("Hydrochloric Acid", 25, 0.1)
vinegar = Acid("Acetic Acid", 20, 0.1, 6.2e-5)
NaOH = Base("Sodium Hydroxide", 0.1)

experiment = ActualTitration(acid=vinegar, base=NaOH)
output_base, output_pH, output_eq_volume, output_pH_eq = experiment.generating_curve()

print(f"Calculated Equivalence Point: {output_eq_volume:.2f} cm³")
experiment.plotting(output_base, output_pH, output_eq_volume, output_pH_eq)