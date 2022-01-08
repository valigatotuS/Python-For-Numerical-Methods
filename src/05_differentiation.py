"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     8/01/2021
* Modified:    /
 
"""

import numpy as np
import scipy.integrate as sciint
import matplotlib.pyplot as plt


def main():
    # Important note : this code is not finished yet and so incorrect, work in progress
    
    (m,g,Cd) = (75,9.81,0.25)
    t = np.arange(0, 11, 1)
    dudt = lambda u: g - ((Cd/m)*u**2)
    dxdt = lambda x: -2 * ((Cd/m)*x)
    
    # plt.plot(x, f(t))
    


# def runge_kutta():
#     sciint.solve_ivp(fun, t_span, y0, options)
#     pass
        
def euler(f1, f2, t):
    rabbit = np.zeros(len(t))
    fox = np.zeros(len(t))
  
    for i in range(len(t)-1):
        rabbit[i+1] = rabbit[i] +  f1(rabbit[i], fox[i])[0]
        fox[i+1] = fox[i] + f1(rabbit[i], fox[i])[1]
        
    plt.plot(t, rabbit)
    
# def Euler(x_prev, y_prev, i):
#     x_new = fun(i*dt, [x_prev, y_prev])[0]*dt + x_prev
#     y_new = fun(i*dt, [x_prev, y_prev])[1]*dt + y_prev
#     x1_values.append(x_new)
#     y1_values.append(y_new)
#     i += 1
#     if (i*dt < end - start):
#         Euler(x_new, y_new, i)
#     else:
#         data1 = [x1_values, y1_values]
#         plotIt(data1, 'Euler', 'b')
#     return
        
def sys(t,y): 
    (m,g,Cd) = (75,9.81,0.25)
    dudt = g - Cd/m*y[0]**2 
    dxdt = y[0] 
    return [dudt,dxdt]

if __name__ == '__main__':
    main()
