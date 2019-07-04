def Gianik(plan):
    for t in range(360):
        j=0
        for i in range(j+1,len(plan)):
            x = (plan[j][0] + plan[j][1]*t) % 360
            y = (plan[i][0] + plan[i][1]*t) % 360
            if x == y:
                return t
        j += 1
    return "GIANIK IS NEVER ECLIPSED"

while True:
    pl = int(input())
    planetas = []
    for i in range(pl):        
        numbers = [int(x) for x in input().split()]        
        a = numbers[1] % 360
        b = numbers[2] % 360
        planetas.append([a,b])
    print(Gianik(planetas))
