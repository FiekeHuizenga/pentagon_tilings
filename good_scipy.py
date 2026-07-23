# This file determines, for a given set X in N^5, whether or not X is good
# Returns True if X is good
# Returns False if X is not good

from scipy.optimize import linprog

# main constraints for X is good
def good_first_constraints(X):
    # variables: u1, ..., u5
    # equalities: A_eq*(u1, u2, u3, u4, u5) = b_eq
    # inequalities: A_ub*(u1, u2, u3, u4, u5) <= b_ub

    # bounds for u
    bounds = [(None, None), (None, None), (None, None), (None, None), (None, None)]

    # sum(u_i) = 0
    A_eq = [[1,1,1,1,1]]
    b_eq = [0]

    # u*v >= 0 for all v in X
    # -u*v <= 0 for all v in X
    A_ub = []
    b_ub = []
    for v in X:
        A_ub.append([-v[0], -v[1], -v[2], -v[3], -v[4]])
        b_ub.append(0)

    return bounds, A_eq, b_eq, A_ub, b_ub

# u*v = 1 for v = X[i]
# Returns False iff there is found a u that satisfies the conditions (i.e. X is not good)
# For X to be good, this function should return True for all i.
def good_second_constraint(i,X):
    # set the basis constraints
    bounds, A_eq, b_eq, A_ub, b_ub = good_first_constraints(X)

    # u*X[i] = 1
    A_eq.append([X[i][0], X[i][1], X[i][2], X[i][3], X[i][4]])
    b_eq.append(1)

    # objective: nothing
    objective = [0,0,0,0,0]

    # solve using linprog
    solution = linprog(objective, A_ub, b_ub, A_eq, b_eq, bounds, method='highs')
    
    if solution.success:
        return False # X is not good
    return True

def is_good(X):
    # If is_good(i,X) returns True for all i, then X is good. 
    solution = all(good_second_constraint(i, X) for i in range(len(X)))
    return solution
