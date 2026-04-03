import numpy as np

class Acid:
    def __init__(self, name, vol, conc, ka=None):    #ka requires a default 'None'
        self.name = name
        self.vol = vol
        self.conc = conc
        self.ka = ka
    
    def pH_calculator(self):
        if self.ka is not None:
            return -0.5*np.log10(self.ka*self.conc)
        else:
            return -np.log10(self.conc)
        
#For testing:
hcl = Acid("Hydrochloric Acid", 25, 0.1)
vinegar = Acid("Acetic Acid", 25, 0.1, 1.8e-5)

#And outputs:
print(f"{hcl.name} initial pH: {hcl.pH_calculator():.2f}")
print(f"{vinegar.name} initial pH: {vinegar.pH_calculator():.2f}")
    

