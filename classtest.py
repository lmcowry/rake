class OldGuessObj:
    oldGuessObjCount = 0

    def __init__(self, guessAt0, guessAt1, guessAt2, guessAt3):
        self.guess0 = guessAt0
        self.guess1 = guessAt1
        self.guess2 = guessAt2
        self.guess3 = guessAt3
        OldGuessObj.oldGuessObjCount += 1

    def displayCount(self):
        printString = ("There are {0} instances of the OldGuessObj class".format(OldGuessObj.oldGuessObjCount))
        print(printString)

    def __str__(self):
        return "hi, i'm an old guess"

x = OldGuessObj(100, 2, 3, 4)
theListOfObj = []
theListOfObj.append(x)
x.displayCount()
y = OldGuessObj(2,3,4,5)
theListOfObj.append(y)
z = OldGuessObj(3,4,5,6)
theListOfObj.append(z)
print(x)
x.displayCount()
print(x.guess0)
for anObj in theListOfObj:
    print(anObj.guess0)
print("that was the first one")

def another():
    z = OldGuessObj(5, 5, 5, 5)
    theListOfObj.append(z)

another()

for anObj in theListOfObj:
    print(anObj.guess0)
print("this is the second")
print(theListOfObj)

# so the objects in the list can have the same name
