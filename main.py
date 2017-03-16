import webapp2, jinja2, os, re, random
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)
listOfOldGuesses = []
approvedGuesses = ["b", "r", "g", "c", "m", "y"]



def aColorValidator(guess):
    if guess in approvedGuesses:
        return True
    else:
        return False

def randomAnswer():
    # answerAt0 = random.choice(approvedGuesses)
    # answerAt1 = random.choice(approvedGuesses)
    # answerAt2 = random.choice(approvedGuesses)
    # answerAt3 = random.choice(approvedGuesses)
    #
    # # probably won't be needed
    # # theAnswer = AnswerObj(answerAt0, answerAt1, answerAt2, answerAt3)
    #
    # theAnswerList = [answerAt0, answerAt1, answerAt2, answerAt3]
    #
    # return theAnswerList
    hardCoded = ["b", "b", "b", "b"]
    return hardCoded


# theAnswerList = randomAnswer()


def currectAnswer(theGuess, theAnswerList):
    # if theGuess.guess0 == theAnswerList[0] and theGuess.guess1 == theAnswerList[1] and theGuess.guess2 == theAnswerList[2] and theGuess.guess3 == theAnswerList[3]:
    if theGuess.guess0 == "b" and theGuess.guess1 == "b" and theGuess.guess2 == "b" and theGuess.guess3 == "b":
        return True
    else:
        return False

# def clueGiver(theGuess, theAnswerList):
#     for (eachPeg in theGuess)


class SuperHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPageHandler(SuperHandler):

    def render_front(self, theAnswerList="", guessAt0="", guessAt1="", guessAt2="", guessAt3="", error="", clues=""):
        theAnswerList = randomAnswer()
        self.render("theModel.html", theAnswerList=theAnswerList, guessAt0=guessAt0, guessAt1=guessAt1, guessAt2=guessAt2, guessAt3=guessAt3, error=error, clues=clues, listOfOldGuesses=listOfOldGuesses)

    def get(self):
        self.render_front()

    def post(self):
        guessAt0 = self.request.get("guessAt0")
        guessAt1 = self.request.get("guessAt1")
        guessAt2 = self.request.get("guessAt2")
        guessAt3 = self.request.get("guessAt3")
        theAnswerList = self.request.get("theAnswerList")

        if aColorValidator(guessAt0) and aColorValidator(guessAt1) and aColorValidator(guessAt2) and aColorValidator(guessAt3):
            thisGuess = OldGuessObj(guessAt0, guessAt1, guessAt2, guessAt3)
            if currectAnswer(thisGuess, theAnswerList):
                self.response.out.write("nice work, you've won")
            # else:
            #     # listOfClues = clueGiver(thisGuess)
            #     listOfOldGuesses.append(thisOldGuess)
            #     self.render_front()
            listOfOldGuesses.append(thisGuess)
            self.render_front()

        else:
            error = "Possible answers are r, g, b, c, m, y.  You fucked up"
            self.render_front(theAnswerList, guessAt0, guessAt1, guessAt2, guessAt3, error)

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

class AnswerObj:
    answerObjCount = 0

    def __init__(self, guessAt0, guessAt1, guessAt2, guessAt3):
        self.guess0 = guessAt0
        self.guess1 = guessAt1
        self.guess2 = guessAt2
        self.guess3 = guessAt3
        AnswerObj.answerObjCount += 1

    def displayCount(self):
        printString = ("There are {0} instances of the AnswerObj class".format(AnswerObj.answerObjCount))
        print(printString)

    def __str__(self):
        return "hi, i'm an answer"


app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)
