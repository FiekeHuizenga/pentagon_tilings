import results as r
import permutations as per

# there are 10 possible rotations and mirrors for any vector in N^5
all_rotations_mirrors = [(0,1,2,3,4), (1,2,3,4,0), (2,3,4,0,1), (3,4,0,1,2), (4,0,1,2,3),
                         (4,3,2,1,0), (0,4,3,2,1), (1,0,4,3,2), (2,1,0,4,3), (3,2,1,0,4)]

# find all rotations/mirrors of X = ((...),(...)). 
def rot_mir(X):
    result = set()
    # choose a rotation/mirror
    for p in all_rotations_mirrors:
        entry_p = []
        # apply this rotation/mirror on all v in X
        for v in X:
            w = tuple(v[p[i]] for i in range(5))
            entry_p.append(w)
        # add entry_p to the result set. Sort it to avoid duplicates.
        result.add(tuple(sorted(entry_p)))
    return result

# find the smallest (canonical) representative of rot_mir(X)
def canonical(X):
    return min(rot_mir(X))

# collect all uniqe representatives
def unique(R):
    result = set()
    for X in R:
        c = canonical(X)
        result.add(c)
    return result

# # round_5 -> 371
# print("number of unique candidate sets: ", len(unique(per.permutations_total(r.round_5))))
