import math

#Day 1 - Calculating the pH of an acid and base solution
def pH_calculator(v_acid, c_acid, v_base, c_base):
    m_acid = (v_acid / 1000)* c_acid    #assuming density = 1.00 gcm^(-3)
    m_base = (v_base / 1000) * c_base
    v_total = v_acid + v_base   #creating v_total now to avoid repeating "v_acid + v_base"

    if any(x < 0 for x in [v_acid, c_acid, v_base, c_base]):
        raise ValueError("Volumes and concentrations should be non-negative.")     #rejecting impossible inputs with `raise ValueError`

    if v_total == 0:
        return 7.00     #the pH of an empty beaker is simply "7.00"
    
    if m_acid > m_base:
        m_acid_excess = m_acid - m_base
        c_proton = m_acid_excess / (v_total / 1000)
        return - math.log10(c_proton)   #condensed 2 lines into 1 by returning the calculation instead a new variable

    elif m_base > m_acid:
        m_base_excess = m_base - m_acid
        c_hydroxide = m_base_excess / (v_total / 1000)
        return 14 + math.log10(c_hydroxide)
    
    else:
        return 7.00

get_v_acid = float(input("Volume of a Strong Monoprotic Acid (mL): "))
get_c_acid = float(input("Concentration of a Strong Monoprotic Acid (dm^-3): "))
get_v_base = float(input("Volume of a Strong Monoprotic Base (mL): "))
get_c_base = float(input("Concentration of a Strong Monoprotic Base (dm^-3): "))

pH = pH_calculator(get_v_acid, get_c_acid, get_v_base, get_c_base)

print(f"The pH of the solution is: {pH:.2f}")
    