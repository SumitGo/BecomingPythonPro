l = [1,2,3,4,5,6,7,8]
sume, sumo = 0,0
print(sume, sumo)
i=0
while i<len(l):
    if i%2==0:
        sume+=l[i]

    else:
        sumo += l[i]

    i+=1

print("Even elements sum: ", sume)
print("Odd elements sum: ", sumo)