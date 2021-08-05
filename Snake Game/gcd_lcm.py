def computeGCD(n1, n2):
    if n1>n2:
        small = n2
    else:
        small = n1
    
    for  i in range(1, small+1):
        if (n1 % i == 0) and  (n2 % i == 0):
            gcd = i
            
    return gcd

def lcm (n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    
    while True:
        if (greater % x == 0) and  (greater % y == 0):
            lcm = greater
            break
        greater += 1
        
    return lcm

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    print(computeGCD(n1, n2), lcm(n1, n2))