import results as r
from itertools import permutations

# this is a list of all possible permutations of 5 elements. Length = 5! = 120
all_permutations = list(permutations([0,1,2,3,4]))

# do the same permutation on all elements of a set X = [[...],[...]].
# output: set {((...),(...),p_1),...,((...),(...),p_120)} containing all permutations of X. 
def permutations_X(X):
    # result will keep a dictionary of which permutation is used
    result = {}
    # choose a permutation
    for p in all_permutations:
        entry_p = []
        # apply this permutation on all v in X
        for v in X:
            w = tuple(v[p[i]] for i in range(5))
            entry_p.append(w)
        # add entry_p to the result set. Sort it to avoid duplicates.
        result.update({tuple(sorted(entry_p)):p})
    return result

# repeat the function above for all X in a list R = [[[...],[...]],[[...],[...]]]
# output: {((...),(...)),((...),(...))} 
# print(len(permutations_total(r.round_5))) = 3495
def permutations_total(R):
    result = {}
    for X in R:
        result.update(permutations_X(X))
    return result

# there are 10 possible rotations and mirrors for any vector in N^5
all_rotations_mirrors = [(0,1,2,3,4), (1,2,3,4,0), (2,3,4,0,1), (3,4,0,1,2), (4,0,1,2,3),
                         (4,3,2,1,0), (0,4,3,2,1), (1,0,4,3,2), (2,1,0,4,3), (3,2,1,0,4)]

def compose(p,q):
    return tuple(p[q[i]] for i in range(5))

# find all rotations/mirrors of X = ((...),(...)). 
def rot_mir(X, p):
    result = {}
    # choose a rotation/mirror
    for q in all_rotations_mirrors:
        entry_pq = []
        # apply this rotation/mirror on all v in X
        for v in X:
            w = tuple(v[q[i]] for i in range(5))
            entry_pq.append(w)
        # add entry_p to the result set. Sort it to avoid duplicates.
        result.update({tuple(sorted(entry_pq)):compose(p,q)})
    return result

# find the smallest (canonical) representative of rot_mir(X)
def canonical_representative(X,p):
    result = {}
    rotmir = rot_mir(X,p)
    canonical = min(rotmir)
    result.update({canonical : rotmir.get(canonical)})
    return result

# collect all uniqe representatives
# print((len(unique(permutations_total(r.round_5))))) = 371
def unique(R):
    result = {}
    for X in R:
        p = R.get(X)
        result.update(canonical_representative(X,p))
    return result

