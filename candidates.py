import numpy as np

# This function computes the set V of eligible vectors
def make_V(u, m):
    V = []
    vmax = [0,0,0,0,0]
    # The bounds for v_1 t/m v_3 are given by m_X
    for i in range(3):
        vmax[i] = int(2 // m[i])
    
    # The bounds for v_4 and v_5 are different if m_X[i] == 0
    for i in (3,4):
        if m[i] != 0:
            vmax[i] = int(2 // m[i])
        else:
            vmax[i] = int((-1 * sum([vmax[j]*max(0,u[j]) for j in range(i)])) // u[i])
    
    # test all options, brute force
    for v_1 in range(vmax[0] + 1):
        for v_2 in range(vmax[1] + 1):
            for v_3 in range(vmax[2] + 1):
                for v_4 in range(vmax[3] + 1):
                    for v_5 in range(vmax[4] + 1):
                        v = [v_1, v_2, v_3, v_4, v_5]
                        if np.inner(v, u) >= 0 and np.inner(v,m) <= 2:
                            V.append(v)
    return V

