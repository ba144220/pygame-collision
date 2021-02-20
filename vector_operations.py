def inner_product(a,b):
    return a[0]*b[0] + a[1]*b[1]

def magnitude(a):
    return (a[0]**2 + a[1]**2)**0.5

def strech(k,a):
    return (k*a[0], k*a[1])

def project(a,b):
    k = inner_product(a,b)/(magnitude(b))**2
    return strech(k,b)

def substract(a,b):
    return (a[0]-b[0], a[1]-b[1])

def mirror(a,b):
    c = project(a,b)
    d = substract(a,c)
    d = strech(2,d)
    return substract(a,d)

def reflect(a,b):
    c = project(a,b)
    d = substract(a,c)
    d = strech(2,d)
    a1 = substract(a,d)
    return strech(-1, a1)

def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

