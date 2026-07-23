# This file computes, for a given finite set X in N^5, the corresponding set compat(X)

import sympy as sp
from fractions import Fraction
import numpy as np

# Function to compute the kernel of a matrix
def compute_kernel(M):
    M = sp.Matrix(M)
    kernel = M.nullspace()
    return [list(v) for v in kernel]

# check if the inproduct with the kernel is always 0
def kernel_check(v,kernel): 
    for k in kernel:
        # if inproduct(v,k) != 0:
        if np.inner(v,k) != 0:
            return False
    return True

# check if alpha*v is close enough to 2
def close_enough(alpha, v, precision):
    product = np.inner(alpha,v)
    return product > 2 - precision and product < 2 + precision


# Function to compute compat(alpha[i])
def compat(X, alpha):
    if X == None:
        return 
    
    compat_X = []
    alpha_frac = [Fraction(alpha[i]).limit_denominator() for i in range(5)]

    # compute the kernel of M
    M = [[1,1,1,1,1]] + X
    kernel = compute_kernel(M)

    # compute the upper bound for each coordinate
    max = [int(2 // alpha[i]) + 1 for i in range(5)]
    
    # test all options, brute force
    for v_1 in range(max[0] + 1):
        sum_1 = v_1*alpha[0]
        for v_2 in range(max[1] + 1):
            sum_2 = sum_1 + v_2*alpha[1]
            if sum_2 > 2.1: 
                break
            for v_3 in range(max[2] + 1):
                sum_3 = sum_2 + v_3*alpha[2]
                if sum_3 > 2.1: 
                    break
                for v_4 in range(max[3] + 1):
                    sum_4 = sum_3 + v_4*alpha[3]
                    if sum_4 > 2.1: 
                        break
                    for v_5 in range(max[4] + 1):

                        v = [v_1, v_2, v_3, v_4, v_5]

                    # check if alpha*v is close to 2
                    # if so, double check if alpha_frac*v == 2
                        if close_enough(alpha,v,0.00000001):
                            if np.inner(alpha_frac, v) == 2 and kernel_check(v,kernel):
                                compat_X.append(v)
    
    return compat_X