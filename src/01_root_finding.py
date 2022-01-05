"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     4/10/2021
* Modified:    5/10/2021
 
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def main():
    f = lambda x: (x**2) - (2*x) - 100
    df = lambda x: 2*x - 2
    (xl, xu) = (float(input("guess xl: ")), float(input("guess xu: ")))
    
    # opti(f,x, guess=0)
    sol_0 = opti(f, (xl+xu)/2)
    sol_1 = bisection(f, xl, xu)
    sol_2 = regula_falsi(f, xl, xu)
    sol_3 = newton_raphson(f, df, (xl+xu)/2)
    
    plot_it(f, np.arange(-30,30), [30+int(sol_0)])
    print(sol_0, sol_1, sol_2, sol_3)

def opti(f, guess):
    r, infodict, ier, msg = optimize.fsolve(f, guess, full_output=True)
    return r[0]

def bisection(f, xl, xu, toll = 1e-6, max_iter = 1000)-> float:
    count = 0
    xr = 1
    
    if(f(xl)*f(xu) > 0):
        raise Exception("The scalars a and b do not bound a root")
    
    while((np.abs(f(xr)) > toll) & (count < max_iter)):
        xr = (xl + xu) * 0.5
        if((f(xl) * f(xr)) < 0): xu = xr
        else:                    xl = xr     
        count += 1
    
    print("Bisection looped ", count, " times.")
    return xr

def newton_raphson(f, df, xr, toll = 1e-6, max_iter = 10000)-> float:
    count = 0
    while((np.abs(f(xr)) > toll) & (count < max_iter)):
        xr -= f(xr)/df(xr)
        count += 1
    print("newton_raphson looped ", count, " times.")
    return xr  

def regula_falsi(f, xl, xu, toll = 1e-6, max_iter = 1000)-> float:
    count = 0
    xr = 1
    
    if(f(xl)*f(xu) > 0):
        raise Exception("The scalars a and b do not bound a root")
    
    while((np.abs(f(xr)) > toll) & (count < max_iter)):
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        if((f(xl) * f(xr)) < 0): xu = xr
        else:                    xl = xr     
        count += 1
    
    print("regula_falsi looped ", count, " times.")
    return xr

def plot_it(f, x, marks):
    y = f(x)
    ax = plt.gca()
    ax.axhline(y=0, color = 'r')
    plt.plot(x, y, markevery=marks, marker='D')
    plt.grid(True)

if __name__ == '__main__':
    main()
