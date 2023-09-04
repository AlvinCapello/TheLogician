def fneg(p):
    return 1 - p

def fcnj(p,q):
    return min(p,q)

def fdisj(p,q):
    return max(p,q)

def fcond(p,q):
    return max(1 - p,q)

def fbic(p,q):
    return 1 - abs(p - q)

def fxor(p,q):
    return abs(p - q)

def fnor(p,q):
    return 1 - max(p,q)

def fnand(p,q):
    return 1 - min(p,q)






