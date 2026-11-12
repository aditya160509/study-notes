treearray = [[-1 for row in range(3)] for (col in range(50))]
FreeNode = 0
RootPointer = -1



def AddNode(number):
    global Freenode 
    global Rootpointer
    global treearray


    if freenode == 0:
        treearray[0][1] = number
        Rootpointer = 0
        freenode =freenode+1
    elif freenode < 49:
        treearray[freenode][1] = number
        for i in range(50):
            if treearray[i][0] == -1:
                treearray[i][0] = Freenode

            elif treearray[i][2] == -1:
                treearray[i][2] = Freenode
                
                 

    freenode = freenode +1 
    print(treaarray)



treearray =[{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}, {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10: -1}, {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10:-1}]
print(treearray, "\n")
print("\n")
call AddNode(55)

         
       
       