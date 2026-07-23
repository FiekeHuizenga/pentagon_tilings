# Goal: find all possible permutations of the found candidate sets. 

from itertools import permutations
import results as r

# this is a list of all possible permutations of 5 elements. Length = 5! = 120
all_permutations = list(permutations([0,1,2,3,4]))

# do the same permutation on all elements of a set X = [[...],[...]].
# output: set {((...),(...)),((...),(...))} containing all permutations of X. 
def permutations_X(X):
    result = set()
    # choose a permutation
    for p in all_permutations:
        entry_p = []
        # apply this permutation on all v in X
        for v in X:
            w = tuple(v[p[i]] for i in range(5))
            entry_p.append(w)
        # add entry_p to the result set. Sort it to avoid duplicates.
        result.add(tuple(sorted(entry_p)))
    return result

# repeat the function above for all X in a list R = [[[...],[...]],[[...],[...]]]
# output: {((...),(...)),((...),(...))} 
def permutations_total(R):
    result = set()
    for X in R:
        per_X = permutations_X(X)
        for per in per_X:
            result.add(per)
    return result

# # R = r.round_5 -> 3495 
# print("number of candidate sets (including mirrors/rotations): ", ((len(permutations_total(R)))))
