def ReadData():
  DataList = []
  FileName = input("Enter the filename")
  try:
    File = open(FileName)
    for Line in File:
      DataList.append(Line)
    File.close()
  except:
    print("Cannot open file")
  return DataList



def SplitData(DataArray):
 Red = []
 Green = []
 Blue = []
 Orange = []
 Yellow = []
 Pink = []
 for Line in DataArray:
   SplitLine = Line.split(",")
 if SplitLine[1].strip() == "red":
  Red.append(SplitLine[0])
 elif SplitLine[1].strip() == "green":
  Green.append(SplitLine[0])
 elif SplitLine[1].strip() == "blue":
  Blue.append(SplitLine[0])
 elif SplitLine[1].strip() == "orange":
  Orange.append(SplitLine[0])
 elif SplitLine[1].strip() == "yellow":
  Yellow.append(SplitLine[0])
 else:
  Pink.append(SplitLine[0])


  def StoreData(datatostore,filename):
    try:
     file = open(filename,"a+")
     for item in datastostore:
      file.write(item + "\n")
      file.close()

    except:
     print("cannotread or write to this file")



     StoreData(Red, "Red.txt")
     StoreData(Green, "Green.txt")
     StoreData(Blue, "Blue.txt")
     StoreData(Orange, "Orange.txt")
     StoreData(Yellow, "Yellow.txt")
     StoreData(Pink, "Pink.txt")

    DataFromFile = ReadData()
    SplitData(DataFromFile)





    class Animal:
        def __init__(self,name,sound,intelligence,size):
          self.name = name
          self.sound = sound
          self.intelligence = intelligence
          self.size = size



        def Description(self):
            Message = ("The animal's name is " + self.name + ", it makes a "
                 + self.sound + ", its size is " + str(self.size)
                 + " and its intelligence level is " + str(self.intelligence))
            return Message



        class Parrot(Animal):
          def _init_(self,wingspan,numberofwords,name,sound,intelligence,size):
            super()._init_(name,sound,intelligence,size)
            self.wingspan = wingspan
            self.numberofwords =numberofwords


            def chnagenumberofwords(self,change):
              self.numberofwords+= change


              def Description(self):
                Message = ("The animal's name is " + self.Name + ", it makes a "
                           + self.Sound + ", its size is " + str(self.Size)
                           + " and its intelligence level is " + str(self.Intelligence)
                           + ". It has a wingspan of " + str(self.WingSpan)
                           + "cm and can say " + str(self.NumberWords) + " words.")
                return Message

















def calculatehash(key):
   return key % 200


class key:
  """Hash-table key with a stable hash value and value-based comparison."""

  def __init__(self, value):
    self.value = value

  def __hash__(self):
    return calculatehash(self.value)

  def __eq__(self, other):
    if not isinstance(other, key):
      return NotImplemented
    return self.value == other.value

  def __repr__(self):
    return f"key({self.value!r})"





  def readdata():
    treeobject=[]

    try:
        file = open(tree.txt,"a+")
