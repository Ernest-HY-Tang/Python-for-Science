import math

#Draft 1: Get the user to input length and did not consider angles
#def pendulum(L):
#    period = 2 * math.pi * math.sqrt(L/9.81)
#    return period

#length = float(input("Length of pendulum: "))

#ideal_period = pendulum(length)

#Draft 2:
lengths = [1, 5, 10, 20, 30, 40, 50, 70, 80, 90]
ideal_periods = []
output_actual = []
for L in lengths:
    ideal_periods.append(2 * math.pi * math.sqrt(L/9.81))

clean_ideal = [round(x, 2) for x in ideal_periods]  #rounding each period to 2dp

def pendulum(get_ideal, d):
    actual_periods = []     #put the empty list IN the function such that the list restarts
    radians = math.radians(d)   #or manually: radians = degrees / 180 * 2 * math.py
    for T in get_ideal:
        actual_periods.append(T * (1 + (radians**2)/16)) #approximation when angle is significant
    return actual_periods

degrees = float((input("The angle that the string is pulled back (in degrees): ")))
raw_actual = pendulum(ideal_periods, degrees)
clean_actual = [round(y, 2) for y in raw_actual]

#errors = [round((b-a)/a*100, 2) for a,b in zip(clean_ideal, clean_actual)]

#print(f"Ideal periods (s): {clean_ideal}")
#print(f"Actual periods (s): {clean_actual}")
#print(f"Percentage errors (%): {errors}")

#Instead, create one big list

print(f"\n{'Length (m)':<12} | {'Ideal (s)':<12} | {'Actual (s)':<12} | {'Error':<12}")
print("-" *55)
for i,j,k in zip(lengths, ideal_periods, raw_actual):
    errors = round((k-j)/k * 100, 2)       #always round the decimals!  also, note that the denominator is the real value
    m = round(j,2)
    n = round(k,2)
    print(f"{i:<12} | {m:<12} | {n:<12} | {errors:<12}%")   #vertical bars to separate




