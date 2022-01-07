"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     7/01/2021
* Modified:    /
 
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.array([0.00,0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50], float)
    y = np.array([0,37,71,104,134,161,185,207,225,239,250], float)
    v = lambda x: np.sqrt(x / 0.075)
    
    sol_1 = v(trap_rule(x, y))
    sol_2 = v(simpson_rule(x, y))
    
    print('trap: ', sol_1, '\nsimp: ', sol_2)
    
    plt.plot(x, y, '--xc')
    plt.title('Kinetic energy arrow')
    plt.xlabel('x [m]')
    plt.ylabel('F [N]', rotation = 0)

def trap_rule(x, y):
    (N, area) = (len(x), 0)
    h = (x[-1]-x[0]) / (N - 1)
    for i in range(N-1):
        area += h * (y[i+1] + y[i]) / 2
    return area

def simpson_rule(x, y):
    (N, area) = (len(x), 0)
    h = (x[-1]-x[0]) / (N - 1)
    area = (h/3)*(y[0] + 2 * sum(y[:N-2:2]) + 4 * sum(y[1:N-1:2]) + y[N-1])
    return area

if __name__ == '__main__':
    main()