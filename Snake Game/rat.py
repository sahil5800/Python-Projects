def number_of_notes(k):
    n=0
    while k>0:
        if k > 100:
            k -= 100
            n += 1
        elif k > 50 and k < 100:
            k -= 50
            n += 1
        elif k > 10 and k < 50:
            k -= 10
            n += 1
        elif k > 5 and k < 10:
            k -= 5
            n += 1
        elif k > 2 and k < 5:
            k -= 2
            n += 1
        elif k >0 and k < 2:
            k -= 1
            n += 1
        elif k == 0:
            return n
            
for _ in range(int(input())):
    print(number_of_notes(int(input())))