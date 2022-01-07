"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     7/10/2021
* Modified:    /
 
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sci
from scipy.interpolate import CubicSpline

def main():
    x = np.array([200,250,300,375,425,475])
    y = np.array([7.5,8.6,8.7,10.0,11.3,12.7])
    xi = np.linspace(x[0],x[-1], 300)
    
    #----------------------solutions----------------------------#
    sol_1 = poly_inter(x,y)
    sol_2 = CubicSpline(x, y)
    sol_3_nnb = sci.interp1d(x, y, kind = "nearest")
    sol_3_lin = sci.interp1d(x, y, kind = "linear")
    sol_3_cub = sci.interp1d(x, y, kind = "cubic")
    sol_4 = np.poly1d(np.polyfit(x, y, 2)) # or greater exp for better fitting
    sol_5 = newton(x,y)
    #-------------------------plots-----------------------------#
    fig, ax = plt.subplots()
    ax.plot(x, y, 'kx', label='known points')    
    #-----sol_1------#
    pol = ax.plot(xi, sol_1(xi), 'r-', label='poly inter')
    #-----sol_2------#
    cubs = ax.plot(xi, sol_2(xi), 'm-', label='cubic spline')
    #-----sol_3------#
    nnb = ax.plot(xi, sol_3_nnb(xi), 'b-', label='nearest neigbour')
    lin = ax.plot(xi, sol_3_lin(xi), 'y-', label='linear')
    cub = ax.plot(xi, sol_3_cub(xi), 'g-', label='cubic')
    #-----sol_4------#
    pfit = ax.plot(xi, sol_4(xi), 'c-', label='poly fit')
    #-----sol_5------#
    newt = ax.plot(xi, sol_5(xi), 'orange', label='newton')
    #---plot style---#
    ax.set_title('Plots: % elongation L as a function of temperature T')
    ax.set_xticks(x)
    ax.set_xlabel('L [%]')
    ax.set_ylabel('T [°C]', rotation = 0)
    ax.legend()

def poly_inter(x, y):
    n = len(x)
    (xN, yN) = (np.zeros([n,n]), y)
    for i in range(n): xN[:,i] = x**i    

    return np.poly1d(np.linalg.solve(xN, yN)[::-1])

def newton(x,y):
    a = y.copy()
    b = [a[0]]
    for e in range(len(x)-1):
        a = [((a[i]-a[i+1])/(x[i]-x[i+1+e])) for i in range(0, len(a)-1)]
        b.append(a[0])
    rslt = [0]
    for i in range(0,len(x)):
        for j in range(0,i):
            b[i] = np.polymul(b[i], [1,-x[j]])
        rslt = np.polyadd(rslt, b[i])
    return np.poly1d(rslt)
    
if __name__ == '__main__':
    main()
