import candidates as can
import compat as com
import good_scipy as g
import angles_scipy as angles_s
import time

# This is the exhaustive search algorithm. It computes all possible candidate sets. 
# Set the max_depth to 4 (or more) to find all possible candidate sets. 
# If you set max_depth > 4, you will get the same result, but it will take longer.
def algorithm_1(X, counter, max_depth):
    calls[0] += 1

    # Find a concrete alpha. If there is no alpha, return. 
    alpha = angles_s.interior_alpha(X)
    if len(alpha) == 0:
        return 

    # compute compat(X) using the alpha we computed and set Y = compat(X)
    Y = com.compat(X, alpha)
    if Y == None:
        return 
    
    # check for duplicates, to reduce the search time
    if Y in treated:
        return
    treated.append(Y)
    amount_treated = len(treated)
    if amount_treated%500 == 0:
        print("amount treated = ", amount_treated)
    
    # check if Y is good and add it to the list of good sets if its not already in there
    if Y != [] and not any(v == Y for v in GOOD_SETS):
        if g.is_good(Y):
            GOOD_SETS.append(Y)
    
    # check counter
    if counter == max_depth:
        return 
    
    # compute m_Y
    min_alph = [angles_s.minimal_alpha(i,Y) for i in range(5)]
    m_Y = [min_alph[i][i] for i in range(5)]

    # compute u
    m_4 = min_alph[3]
    m_5 = min_alph[4]

    if m_Y[3] == 0:
        u = [m_4[i] - alpha[i] for i in range(5)]
    if m_Y[4] == 0 and m_Y[3] > 0:
        u = [m_5[i] - alpha[i] for i in range(5)]
    if m_Y[3] > 0 and m_Y[4] > 0:
        u = [0,0,0,0,0]

    # compute the set of eligible vectors V
    V = can.make_V(u,m_Y)

    # for all w in V: repeat algorithm_1 with X = Y + w
    for w in V:
        if w not in Y:
            X_new = Y + [w]
            algorithm_1(X_new, counter+1, max_depth)

    return 


start = time.time()
treated = []
GOOD_SETS = []
calls = [0]
algorithm_1([],0,4)
print("good sets: ", GOOD_SETS)
print("number of good sets: ", len(GOOD_SETS))
end = time.time()

print("time = ", end-start)
