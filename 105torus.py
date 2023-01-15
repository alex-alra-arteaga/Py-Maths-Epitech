#!/usr/bin/python3

import math
import sys
from typing import List

# ! falta match the output --> sometimes add 0 and somtimes no xd

def torus():

    a = [float(sys.argv[6]), float(sys.argv[5]), float(sys.argv[4]), float(sys.argv[3]), float(sys.argv[2])]
    option = sys.argv[1]
    precission = int(sys.argv[7])

    def bisect_solve(a: List[float], precission, epsilon=1e-6):
        def f(x):
            return a[0]*x**4 + a[1]*x**3 + a[2]*x**2 + a[3]*x + a[4]
        a_0, a_1 = 0, 1
        m = (a_0 + a_1) / 2
        while abs(f(m)) > epsilon:  
            print(f"x = {round(m, precission)}")
            if f(m)*f(a_0) < 0:
                a_1 = m
            else:
                a_0 = m
            m = (a_0 + a_1) / 2
        print(f"x = {round(m, precission)}")
        return m

    def newton_solve(a: List[float], precission, x_0=0.5, epsilon=1e-6):
        def f(x):
            return a[0]*x**4 + a[1]*x**3 + a[2]*x**2 + a[3]*x + a[4]
        def f_prime(x):
            return 4*a[0]*x**3 + 3*a[1]*x**2 + 2*a[2]*x + a[3]
        x_n = x_0
        print(f"x = {round(x_n, precission)}")
        while abs(f(x_n)) > epsilon:
            x_n = x_n - f(x_n)/f_prime(x_n)
            print(f"x = {round(x_n, precission)}")
        print(f"x = {round(x_n, precission)}")
        return x_n

    def secant_solve(a: List[float], precission, x_0=0, x_1=1, epsilon=1e-6):
        def f(x):
            return a[0]*x**4 + a[1]*x**3 + a[2]*x**2 + a[3]*x + a[4]

        x_n_1 = x_0
        x_n = x_1
        while abs(f(x_n)) > epsilon:
            if x_n != 1:
                print(f"x = {round(x_n, precission)}")
            temp = x_n
            x_n = x_n - f(x_n)*(x_n - x_n_1)/(f(x_n) - f(x_n_1))
            x_n_1 = temp
        print(f"x = {round(x_n, precission)}")
        print(f"x = {round(x_n, precission)}")
        return x_n

    # error handling
    argc = len(sys.argv)
    ## no arguments
    if argc <= 1:
        exit(84)
    ##no enough arguments
    if argc < 8:
        exit(84)
    ## to menny argumetns
    if argc > 8:
        exit(84)
    #
    ##bad option
    if int(sys.argv[1]) not in [1, 2, 3]:
        exit(84)
    #
    ##chech for invalid arguments
    for num in sys.argv[1:]:
        try:
            int(num)
        except ValueError:
            exit(84)

    if (option == '1'):
        bisect_solve(a, precission)
    if (option == '2'):
        newton_solve(a, precission)
    if (option == '3'):
        secant_solve(a, precission)

torus()
