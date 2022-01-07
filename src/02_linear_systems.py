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
* Modified:    /
 
"""

import numpy as np
import scipy

def main():
    A = np.array([[5.5,3.5,2.5],[3,5,2],[1.5,3,5.5]])
    b = np.array([15e3, 13.2e3, 14.5e3])
    
    sol_0 = np.linalg.solve(A,b)
    sol_1 = forward_elim(np.copy(A), np.copy(b))
    sol_2 = lu_factorization(A, b)
    sol_3 = jacobi(A, b)
    
    [print("\n >", sol,"\n") for sol in [sol_0, sol_1, sol_2, sol_3]]
    
def forward_elim(A,b)->(np.ndarray,np.ndarray):
    for i in range(0, A.shape[0]):
        for j in range(0, A.shape[1]):
            if not (j > i) or A[i][i] == 0: continue
            mul = A[j,i]/A[i,i]
            b[j] -= b[i] * mul 
            A[j] -= A[i] * mul
            
    norm_diag(A, b)
    return (A,b)

def norm_diag(A:np.ndarray,b:np.ndarray)->None:
    for i in range(A.shape[0]):
        b[i] /= A[i][i]
        A[i] /= A[i][i]

def lu_factorization(A, b)->np.ndarray:
    (p, L, U) = scipy.linalg.lu(A)
    d = np.linalg.solve(L, b)
    x = np.linalg.solve(U, d)
    return x

def jacobi(A,b, max_iter = 1000, x = None, toll=1e-4):
    if x == None:
        x = np.zeros(len(A[0]))
    
    D = np.diag(A)
    R = A - np.diagflat(D)
    cnt = 0
    
    for e in range(max_iter):
        x_prev = np.copy(x)
        x = (b- np.dot(R, x)) / D
        delta_x = abs(x[0]-x_prev[0])
        if(delta_x < toll):
            cnt = e+1
            break
    if cnt != 0:
        print("Jacobi looped ", cnt, " times.")
    else:
        print("Jacobi reached max_iter, N=", max_iter)
    return x


if __name__ == '__main__':
    main()
