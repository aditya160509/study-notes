treearray = [[-1 for row in range(3)] for (col in range(50))]
freeNode = 0
RootPointer = -1



def AddNode(number):
    global freenode 
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
                
                 

    freenode  = freenode + 1
        

         
       
treearray=