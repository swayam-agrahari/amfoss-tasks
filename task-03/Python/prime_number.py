import  math
n = int(input("Enter a num: \n"))
if(n < 2):
    print("No prime")
else:
    for i in range (2,n+1):
        flag = 0
        for j in range( 2,int(math.sqrt(i))+1):
            if(i % j == 0):
                flag = 1
                break
        
        if(flag == 0 ):
            print(i, end= " ")
