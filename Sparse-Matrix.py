r = int(input())
c = int(input())
if r*c > 0:
    a = []
    for i in range(c):
       a.append(0)
    main = []
    for i in range(r):
         main.append(a)
    count = 0
    for i in range(r):
       for j in range(c):
            main[i][j] = int(input())
            if main[i][j] == 0:
               count += 1
    nz = r*c - count
    if count >= nz:
      print("Sparse")
    else:
      print("Not sparse")
else:
    print("Invalid input")