def close(n,matrix):
    result=[]
    for row in matrix:
        new_row=[]
        for num in row:
            remainder=num%5
            if remainder<=2:
                near=num-remainder
            elif remainder==3 or remainder==4:
                near=num+(5-remainder)
            else:
                near=num
            new_row.append(near)
        result.append(new_row)
    return result

if __name__=="__main__":
    n=int(input().strip())
    matrix=[]

    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))

    result=close(n,matrix)

    for row in result:
        print(" ".join(map(str,row)))