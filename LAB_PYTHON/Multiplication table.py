def multiplication_table(line,col) :
    cal = line * col
    space = 0
    while cal > 0 :
        cal = cal//10
        space += 1
    for j in range(1,line+1):
        numinline = j * col
        for i in range(j,numinline + 1,j) :
            cal_space = 0
            temp = i
            while temp > 0 :
                temp = temp//10
                cal_space += 1
            cal_space = space - cal_space
            for r in range(cal_space):
                print(end=" ")
            print(i,end=" ")
        print("\n")
multiplication_table(10,10)
