class Record:
    def __init__(self,key,item,item2):
        self.__key = key
        self.__item = item
        self.__item2 = item2


        def GetKey(self):
             return self.__Key
             def GetItem1(self):
              return self.__Item1


        def GetItem2(self):
          return self.__Item2


        Hashtable = []
        spare = []
        def Initialise():
         global HashTable
         global Spare
        for X in range(200):
         Hashtable.append(Record(-1,-1,-1))
         for X in range(100):
             spare.append(Record(-1,-1,-1))

def calculatehash(key):
        return key %200


def InsertIntoHash(TheRecord):
    global HashTable
    global Spare

    HashValue = calculatehash(TheRecord.GetKey())

    if HashTable[HashValue].GetKey() == -1:
        HashTable[HashValue] = TheRecord

    else:
        for x in range(0, 100):
            if Spare[x].GetKey() == -1:
                Spare[x] = TheRecord
                break
        