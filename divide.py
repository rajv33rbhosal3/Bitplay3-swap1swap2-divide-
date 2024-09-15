def d(div,divis):
    s = (-1 if ((div<0)^(div<0))else 1)
    div = abs(div)
    divis = abs(divis)
    qn = 0
    n = 0
    for i in range(31,-1,-1):
        if (n + (divis <<i)<=div):
            n = n + divis << i
            qn |= 1<<i
    if s == -1:
        qn = -qn
    return qn
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print(d(a,b))


    