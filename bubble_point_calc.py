import math

import numpy as np


def BUBL_T(A1, B1, C1, A2, B2, C2, Tn1, Tn2, x1, P):
    i = 0
    T = (Tn1 + Tn2)/2
    while i == 0:
        T_init = T
        exp_1 = A1 - (B1/(T-273+C1))
        print(exp_1)
        exp_2 = A2 - (B2/(T-273+C2))
        print(exp_2)
        exp_diff = np.exp(exp_1) - np.exp(exp_2)
        print(exp_diff)
        T = B2/(A2 - np.log(P-(x1*exp_diff))) - C2
        differ = T - T_init
        diff_error = (differ/T_init)*100
        print(diff_error)
        print("Iter "+str(i))
        if abs(diff_error) <= 1:
            i = 1
    return T


# while True: #Quick Error Checking. Will need to convert into function that also checks for non-negative as well as defaults and can be applied against all variables.
'''
A1 = float(input("Enter A1 value: "))
B1 = float(input("Enter B1 value: "))
C1 = float(input("Enter C1 value: "))
A2 = float(input("Enter A2 value: "))
B2 = float(input("Enter B2 value: "))
C2 = float(input("Enter C2 value: "))
Tn1 = float(input("Enter Tn1 value: "))
Tn2 = float(input("Enter Tn2 value: "))
x1 = float(input("Enter x1: "))
P = float(input("Enter P: "))
'''
A1 = 13.7667
B1 = 2451.88
C1 = 232.014
A2 = 13.8193
B2 = 2696.04
C2 = 224.317
Tn1 = 309.2
Tn2 = 341.9
x1 = 0.63
P = 331.5
T = BUBL_T(A1, B1, C1, A2, B2, C2, Tn1, Tn2, x1, P)

print("Temperature is {}".format(T))
'''
A1 = 13.7667 
B1 = 2451.88
C1 = 232.014
A2 = 13.8193
B2 = 2696.04
C2 = 224.317
Tn1 = 309.2
Tn2 = 341.9
x1 = 0.63
P = 331.5
'''
