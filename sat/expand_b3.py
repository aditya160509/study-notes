class Bird:
 def __init__(self, DistancePerHour, Species):
  self.__Species = Species #string
  self.__DistancePerHour = DistancePerHour #real
  self.__XPosition = 500.0 #real
  self.__YPosition = 500.0 #real


def getspecies(self):
  return self.__Species

def getdistanceperhour(self):
  return self.__DistancePerHour

def GetPosition(self):
 ReturnValue = "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)
 return ReturnValue

def move (self,direction,flyingmin):
    if direction == "N":
     self.__YPosition = self.__YPosition + ((self.__DistancePerHour * flyingmin / 60)*flyingmin)
    elif direction == "S":
     self.__YPosition = self.__YPosition - ((self.__DistancePerHour * flyingmin / 60)*flyingmin)
    elif direction == "E":
     self.__XPosition = self.__XPosition + ((self.__DistancePerHour * flyingmin / 60)*flyingmin)
    elif direction == "W":
     self.__XPosition = self.__XPosition - ((self.__DistancePerHour * flyingmin / 60)*flyingmin)


bird1 = Bird(71, "cockatiel")
bird2 = Bird(56, "macaw")

print(bird1.getspecies(), "is currently at", bird1.GetPosition())
print(bird2.getspecies(), "is currently at", bird2.GetPosition())

choice = 0
while choice != 1 and choice != 2:
    choice = int(input("Which bird do you want to move? Enter 1 or 2: "))

flyingmin = -1
while flyingmin < 0 or flyingmin > 500:
    flyingmin = int(input("How many minutes has the bird been flying? "))

valid = False
while valid == False:
    valid = True
    direction = input("Enter direction North, South, East or West: ").upper()

    if direction == "NORTH" or direction == "N":
        if choice == 1:
            bird1.move("N", flyingmin)
        else:
            bird2.move("N", flyingmin)

    elif direction == "SOUTH" or direction == "S":
        if choice == 1:
            bird1.move("S", flyingmin)
        else:
            bird2.move("S", flyingmin)

    elif direction == "EAST" or direction == "E":
        if choice == 1:
            bird1.move("E", flyingmin)
        else:
            bird2.move("E", flyingmin)

    elif direction == "WEST" or direction == "W":
        if choice == 1:
            bird1.move("W", flyingmin)
        else:
            bird2.move("W", flyingmin)

    else:
        valid = False

print(bird1.getspecies(), "is currently at", bird1.GetPosition())
print(bird2.getspecies(), "is currently at", bird2.GetPosition())
             