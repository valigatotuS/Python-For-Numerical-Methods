"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
 

* Author:      valigatotuS
* Created:     5/01/2022
* Modified:    9/01/2022
 
"""

import numpy as np
import scipy

def main():
    #------------------------input------------------------------#
    A = np.array([[5.5,3.5,2.5],[3,5,2],[1.5,3,5.5]])
    b = np.array([15e3, 13.2e3, 14.5e3])
    #----------------------solutions----------------------------#
    sol_0 = np.linalg.solve(A,b) # or np.dot(np.linalg.inv(A),b) 
    sol_1 = forward_elim(np.copy(A), np.copy(b))
    sol_2 = lu_factorization(A, b)
    sol_3 = jacobi(A, b)
    
    [print("\n >", sol,"\n") for sol in [sol_0, sol_1, sol_2, sol_3]]
    
def forward_elim(A,b)->(np.ndarray,np.ndarray):
    for i in range(0, A.shape[1]):
        for j in range(i+1, A.shape[0]):
            if(A[i][i] == 0): continue   # preventing dividing by 0
            mul = A[j,i]/A[i,i]
            b[j] -= b[i] * mul 
            A[j] -= A[i] * mul 
    # norm_diag(A, b)
    return (A,b)

def lu_factorization(A, b)->np.ndarray:                            # efficient for matrices with < dims
    (p, L, U) = scipy.linalg.lu(A)
    d = np.linalg.solve(L, b)
    x = np.linalg.solve(U, d)
    return x

def jacobi(A,b, max_iter = 1000, x = None, toll=1e-4)->np.ndarray: # efficient for diag dom matrices & > dims
    if x == None: x = np.zeros(len(A[0]))
    D = np.diag(A)
    R = A - np.diagflat(D)
    (cnt, delta_x) = (0, 1)

    while(delta_x > toll):
        x_prev = np.copy(x)
        x = (b- np.dot(R, x)) / D
        delta_x = abs(x[0]-x_prev[0])
        cnt += 1
        
    if cnt != 0: print("Jacobi looped ", cnt, " times.") # jacobi will loop less if diagonal is dominant, try it!
    else:        print("Jacobi reached max_iter, N=", max_iter)
    return x

def norm_diag(A:np.ndarray,b:np.ndarray)->None:
    D = np.diag(A)
    b /= D
    A /= D
    # for i in range(A.shape[0]):
    #     b[i] /= A[i][i]
    #     A[i] /= A[i][i]

if __name__ == '__main__':
    main()
