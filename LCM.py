def lcm(x,y):
    lcmm=0
    if x>y:
        great=x
    else:
        great=y
    while(True):
        if(great%x==0 and great%y==0):
            lcmm=great
        else:
            great+=1
    return lcmm
x=int(input())
y=int(input())
print(lcm(x,y))
