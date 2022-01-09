"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     8/01/2022
* Modified:    9/01/2022
 
"""

import numpy as np
import scipy.integrate as sciint
import matplotlib.pyplot as plt


def main():
    #------------------------input------------------------------#    
    (m,g,Cd) = (75,9.81,0.25)
    t = np.arange(0, 11, 1)
    dudt = lambda u: g - ((Cd/m)*u**2)
    # dxdt = lambda x: -2 * ((Cd/m)*x)
    #----------------------solutions----------------------------#
    sol_1 = euler([0,0], t, fun1)
    sol_2 = runge_kutta_45([0,0], t, fun2)
    #-------------------------plots-----------------------------#    
    plt.plot(t, sol_1, label="euler")
    plt.plot(t, sol_2.y[0], label="runge kutta 45")
    plt.title("Euler & Runge Kutta")
    plt.legend(True)
    
def euler(y0, t, fun1):
    d = np.copy(t)
    v = np.copy(t)
    for i in range(len(d)-1):
        d[i+1] = d[i] + fun1(d[i], v[i])[0]
        v[i+1] = v[i] + fun1(d[i], v[i])[1]
    return d
    
def runge_kutta_45(y0, t, fun2):
    return sciint.solve_ivp(fun2, [0,10], y0, t_eval = t, method = 'RK45') 
    
def fun1(x,u):
    dxdt = u
    dudt = 9.81 - (0.25/75)*u**2
    return dxdt,dudt

def fun2(x,u):
    dxdt = u[1]
    dudt = 9.81 - (0.25/75)*u[1]**2
    return dxdt,dudt

if __name__ == '__main__':
    main()