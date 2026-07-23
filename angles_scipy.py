# This file finds, given a finite set X in N^5:
# - an angle-vector alpha in (0,1)^5 with alpha_i >= alpha_i+1 corresponding to X
# - the minimal value m_X_i that alpha_i can have 

from scipy.optimize import linprog

def basis_constraints():
    # variables: alpha1, ..., alpha5
    # equalities: A_eq*(alpha1, alpha2, alpha3, alpha4, alpha5) = b_eq
    # inequalities: A_ub*(alpha1, alpha2, alpha3, alpha4, alpha5) <= b_ub

    # bounds for alpha1, ..., alpha5
    bounds = [(0, None), (0, None), (0, None), (0, None), (0, None)]

    # sum(alpha) = 3
    A_eq = [[1,1,1,1,1]]
    b_eq = [3]

    # alpha[i] >= alpha[i+1] 
    # --> -alpha[i] + alpha[i+1] <= 0
    A_ub = [[-1,1,0,0,0], [0,-1,1,0,0], [0,0,-1,1,0],[0,0,0,-1,1]]
    b_ub = [0,0,0,0]

    # alpha1 <= 1
    A_ub.append([1,0,0,0,0])
    b_ub.append(1)

    return bounds, A_eq, b_eq, A_ub, b_ub


def minimal_alpha(i,X):
    # variables: alpha1, ..., alpha5
    # equalities: A_eq*(alpha1, alpha2, alpha3, alpha4, alpha5) = b_eq
    # inequalities: A_ub*(alpha1, alpha2, alpha3, alpha4, alpha5) <= b_ub

    bounds, A_eq, b_eq, A_ub, b_ub = basis_constraints()

    # v * alpha = 2 for all v in X
    for v in X:
        A_eq.append([v[0], v[1], v[2], v[3], v[4]])
        b_eq.append(2)

    # objective: minimize alpha_i
    objective = [0,0,0,0,0]
    objective[i] = 1

    # solve using linprog
    solution = linprog(objective, A_ub, b_ub, A_eq, b_eq, bounds, method='highs')
    
    if solution.success: 
        return solution.x
    return


def interior_alpha(X):
    # variables: alpha1, ..., alpha5, epsilon
    # equalities: A_eq*(alpha1, alpha2, alpha3, alpha4, alpha5, epsilon) = b_eq
    # inequalities: A_ub*(alpha1, alpha2, alpha3, alpha4, alpha5, epsilon) <= b_ub

    # objective: maximize epsilon (i.e. minimize -epsilon)
    objective = [0,0,0,0,0,-1]

    # bounds for alpha1, ..., alpha5 and epsilon
    bounds = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None)]

    # sum(alpha) = 3
    A_eq = [[1,1,1,1,1,0]]
    b_eq = [3]

    # v * alpha = 2 for all v in X
    for v in X:
        A_eq.append([v[0], v[1], v[2], v[3], v[4], 0])
        b_eq.append(2)

    # alpha[i] >= alpha[i+1] 
    # --> -alpha[i] + alpha[i+1] <= 0
    A_ub = [[-1,1,0,0,0,0], [0,-1,1,0,0,0], [0,0,-1,1,0,0],[0,0,0,-1,1,0]]
    b_ub = [0,0,0,0]

    # alpha1 <= 1-epsilon
    # --> alpha1 + epsilon <= 1
    A_ub.append([1,0,0,0,0,1])
    b_ub.append(1)

    # alpha5 >= epsilon
    # --> epsilon - alpha5 <= 0 
    A_ub.append([0,0,0,0,-1,1])
    b_ub.append(0)

    # solve using linprog
    solution = linprog(objective, A_ub, b_ub, A_eq, b_eq, bounds, method='highs')
    
    if solution.success: 
        # check if epsilon is 0 or not. If epsilon is 0, there is no interior alpha
        if solution.x[5] == 0:
            return []
        else: 
            return solution.x[0:5]
    return []