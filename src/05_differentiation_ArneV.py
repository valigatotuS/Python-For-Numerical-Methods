import numpy as np
import scipy.integrate as scp
import matplotlib.pyplot as plt

h = 0.5
t = np.arange(0, 30 + h, h)
y_begin = [610, 22]

a = 0.23
b = 0.0133
c = 0.4
d = 0.0004

def main():
    " V Arne, label D "
    sol_1 = euler()
    sol_2 = RK45()
    
def euler():
    rabbit = np.zeros(len(t))
    rabbit[0] = y_begin[0]
    fox = np.zeros(len(t))
    fox[0] = y_begin[1]

    for i in range(len(t)-1):
        rabbit[i+1] = rabbit[i] + h * fun1(rabbit[i], fox[i])[0]
        fox[i+1] = fox[i] + h * fun1(rabbit[i], fox[i])[1]
        #print(fun1(rabbit[i], fox[i]))
        
    plt.plot(t, rabbit)
    
def RK45():
    """" rabbit = y[0], fox = y[1] """
    sol = scp.solve_ivp(fun2, [0, 30], y_begin, method = "RK45", t_eval = t)
    #print(sol.y[0])

    plt.plot(t, sol.y[0])
    
def fun1(x, y):
        dxdt = a*x - b*x*y
        dydt = -c*y + d*x*y
        return [dxdt, dydt]
    
def fun2(t, y):
    dxdt = a*y[0] - b*y[0]*y[1]
    dydt = -c*y[1] + d*y[0]*y[1]
    return [dxdt, dydt]
    
if __name__ == "__main__":
    main()