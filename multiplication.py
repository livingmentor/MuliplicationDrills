import random as rnd
from datetime import datetime

class problem:
    #creates a logical representation of a multiplication problem
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ans = x * y
        
        
def problemFactory(num):
    #Factory that returns a list of multiplication problems based on the num parameter 
    probs = []
    for i in range(13):
        probs.append(problem(num, i))
    return probs    

def selProbs():
    #function that allows the user to select the problems that it returns as a list
    selector = input("What number would you like to practice? (0-12 or All) ")
    if selector.upper() == "ALL":
        #returns a complete 0-12 times table
        probs = []
        for i in range(13):
            probs += problemFactory(i)
    else:
        #returns a single row from the times table based on selection
        try:
            i = int(selector) 
            if i >= 0 and i <=12:
                probs = problemFactory(i)
            else:
                probs = []
        except:
            probs = []
    return probs
        
def game():
    problems = selProbs() # runs  the selector
    rnd.shuffle(problems)
    incorrect = []
    runOnce = False
    #For each problem allows the user to hazard a guess
    start = datetime.now()
    for prob in problems:
        runOnce = True
        try:
            resp = int(input("{} X {} = ".format(prob.x, prob.y)))
        except:
            print("Incorrect, {} X {} = {}".format(prob.x, prob.y, prob.ans))
            incorrect.append(prob)
            continue
        if resp == prob.ans:
            print("Correct!")
        else:
            print("Incorrect, {} X {} = {}".format(prob.x, prob.y, prob.ans))
            incorrect.append(prob)
    #After the game is over, it prints the time taken and areas for improvement
    if runOnce == True:
        print('Time taken: {} seconds'.format((datetime.now()- start).seconds))
        for prob in incorrect:
            print("Remember {} X {} = {} for next time".format(prob.x, prob.y, prob.ans))
    else:
        pass
    
def main():
    #main code.  Runs the game and asks the user if they want to continue
    run = True
    while run == True:
        game()
        tryAgain = input("Try again? (Y or N, Default: N) ")
        try:
            if tryAgain.upper() != 'Y':
                run = False
        except:
            run = False
    
if __name__ == "__main__":
    main()

    

