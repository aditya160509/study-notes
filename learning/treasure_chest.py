class TreasureChest:
    # private question : String
    # private answer : Integer
    # private points : Integer

    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = int(answer)
        self.__points = int(points)

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        return self.__answer == int(answer)

    def getPoints(self):
        return self.__points


arrayTreasure = []


def readData():
    filename = "TreasureChestData.txt"

    try:
        file = open(filename, "r")
        dataFetched = file.readline().strip()

        while dataFetched != "":
            question = dataFetched
            answer = file.readline().strip()
            points = file.readline().strip()

            arrayTreasure.append(
                TreasureChest(question, answer, points)
            )

            dataFetched = file.readline().strip()

        file.close()

    except IOError:
        print("Could not find file")


def main():
    readData()

    questionNumber = int(
        input("Pick a question to answer (1-" + str(len(arrayTreasure)) + "): ")
    )

    if 1 <= questionNumber <= len(arrayTreasure):
        chest = arrayTreasure[questionNumber - 1]
        print(chest.getQuestion())

        userAnswer = int(input("Your answer: "))

        if chest.checkAnswer(userAnswer):
            print("Correct! You scored", chest.getPoints(), "points.")
        else:
            print("Incorrect.")
    else:
        print("Invalid question number")


main()