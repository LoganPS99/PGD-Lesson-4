list1=["peanuts","strawberry","mouse","keyboard","phone"]
print(list1[0])
print(list1[-1])
list1.append("charger")
print(list1)
list1.insert(2,"Bob")
print(list1)
list1.pop()
print(list1)
list1.pop(1)
print(list1)
list1.remove("mouse")
print(list1)

#2d List
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print("Number of rows:",len(matrix))
print("Number of coloumns",len(matrix[0]))
print(matrix[1][1])
print(matrix[2][0])

for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print("\n")

matrixA=[[1,2],[3,4]]
matrixB=[[5,6],[8,9]]
result=[[0,0],[0,0]]

for i in range(0,2):
    for j in range(0,2):
        result[i][j]=matrixA[i][j]+matrixB[i][j]

print(result)
