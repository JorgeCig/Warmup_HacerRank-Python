def plusMinus(n,arr):
    cnp, cnn, cz =0, 0, 0
    for num in range(n):
        if arr[num]>0:
            cnp +=1
        elif arr[num]<0:
            cnn +=1
        elif arr[num]== 0:
            cz +=1
        else:
            pass
    return f'{cnp/n}\n{cnn/n}\n{cz/n}'

n = 6
arr = [-4,3,-9,0,4,1] 

print(plusMinus(n,arr))