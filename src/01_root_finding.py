"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     4/01/2021
* Modified:    9/01/2021
 
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

def main():
    #------------------------input------------------------------#
    f = lambda x: (x**2) - (2*x) - 100
    df = lambda x: 2*x - 2
    (xl, xu) = (float(input("guess xl: ")), float(input("guess xu: ")))
    #----------------------solutions----------------------------#
    sol_0 = opti(f, (xl+xu)/2)
    sol_1 = bisection(f, xl, xu)
    sol_2 = regula_falsi(f, xl, xu)
    sol_3 = newton_raphson(f, df, (xl+xu)/2)
    print(sol_0, sol_1, sol_2, sol_3)
    #-------------------------plots-----------------------------#
    plot_it(f, np.arange(-30,30), mark=[sol_0,0])

def opti(f, guess):
    return sci.optimize.root(f, -20)['x'][0]

def bisection(f, xl, xu, toll = 1e-6, max_iter = 1000)->float:
    count = 0
    xr = 1
    
    if(f(xl)*f(xu) > 0):
        raise Exception("The guesses xl and xu do not bound a root, try again")
    
    while((np.abs(f(xr)) > toll) & (count < max_iter)): # normally no need for max_iter because it will always converge
        xr = (xl + xu) * 0.5
        if((f(xl) * f(xr)) < 0): xu = xr
        else:                    xl = xr     
        count += 1
        # plt.plot([xl,xu],[f(xl),f(xu)],'m-') # showing trials
    
    print("bisection looped ", count, " times.")
    return xr

def newton_raphson(f, df, xr, toll = 1e-6, max_iter = 10000)->float:
    count = 0
    while((np.abs(f(xr)) > toll) & (count < max_iter)):
        xr -= f(xr)/df(xr)
        count += 1
    print("newton_raphson looped ", count, " times.")
    # plt.plot([xr],[f(xr)],'mx') # showing trials
    return xr  

def regula_falsi(f, xl, xu, toll = 1e-6, max_iter = 1000)-> float:
    count = 0
    xr = 1
    
    if(f(xl)*f(xu) > 0):
        raise Exception("The guesses xl and xu do not bound a root, try again")
    
    while((np.abs(f(xr)) > toll) & (count < max_iter)):
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        if((f(xl) * f(xr)) < 0): xu = xr
        else:                    xl = xr     
        count += 1
        # plt.plot([xl,xu],[f(xl),f(xu)],'m-') # showing trials
    
    print("regula_falsi looped ", count, " times.")
    return xr

def plot_it(f, x, mark=[0,0]):
    y = f(x)
    plt.gca().axhline(y=0, color = 'gray')
    plt.plot(x, y, 'b-', [mark[0]], [mark[1]], 'ro')
    plt.grid(True)

if __name__ == '__main__':
    main()
