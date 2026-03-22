import math
#def f(u,a,t):
#    print("v="); return u+a*t
#    return u*t + 0.5*a*t**2
#print(f(1,2,3))

def suvat(u,a,t):   #define name of function
    v = u + a*t
    s = u*t + 0.5*a*(t**2)  #use brackets
    return v,s  #tuple, such that it 'returns' both

#float the inputs
initial_u = float(input("Initial velocity: "))
initial_a = float(input("Acceleration1: "))
initial_t = float(input("Time taken: "))

#This should be after the inputs
final_v, final_s = suvat(initial_u,initial_a,initial_t) #to unpack the tuple

print(f"The final velocity is: {final_v:.2f}") #:.3f is 3 decimal places
print(f"The final displacement is: {final_s:.4f}")