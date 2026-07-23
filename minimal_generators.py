# This function finds all minimal generators X of a maximal good set Y. 
# i.e. compat(X) = Y and X has the least length possible. 

import results as r
import compat as com
import angles_scipy as angles_s
from itertools import combinations
import dictionary as d

# find inverse of a permutation
def inv(perm):
    inverse = [0,0,0,0,0]
    for i, p in enumerate(perm):
        inverse[p] = i
    return tuple(inverse)

# check if X generates Y (i.e. compat(X) = Y)
def generates_Y(X, p, Y):
    # first permutate X back to the original
    Y_original = []
    for v in Y:
        w = tuple(v[inv(p)[i]] for i in range(5))
        Y_original.append(w)
    # compute alpha
    alpha_original = angles_s.interior_alpha(Y_original)
    # permute alpha
    alpha = tuple(alpha_original[p[i]] for i in range(5))
    # compute compat(X)
    comp_X = com.compat(X, alpha)

    # check if compat(X) = Y
    # rewrite as a set of tuples, so order doesn't matter
    if {tuple(v) for v in comp_X} == {tuple(v) for v in Y}:
        return True
    return False

def min_generators(Y,p):    
    # try to find a generator X of size 1. 
    # If that doesn't work, try to find a generator of size 2. And so on. 
    for i in range(1, len(Y) + 1):
        # check for all combinations of i vectors of Y if they generate Y
        for X in combinations(Y, i):
            # combinations returns tuples, so convert back to a list:
            X = list(X)
            if generates_Y(X, p, Y) == None:
                return
            if generates_Y(X, p, Y):
                return X
    return None

def min_generators_2(Y,p,size):
    #find a generator of size i
    for X in combinations(Y,size):
        X = list(X)
        if generates_Y(X, p, Y) == None:
            return
        if generates_Y(X, p, Y):
            return X
    return None

dictionary = d.unique(d.permutations_total(r.round_5))
n = 0
for Y in dictionary:
    n += 1
    p = dictionary.get(Y)
    generator = min_generators(Y,p)
    print(n, generator)


