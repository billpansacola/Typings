from keyboard import on_press
from pynput.keyboard import Key, Listener, Controller
from Words import Words

class Game:

    def __init__(self, int):
        self.words = Words().generateWords(int)
        self.displayText = Words().convertListToString(self.words)

    def compare(self, words, input):
        if not(len(words) == len(input)):
            return False
        
        for i in range(0, len(words)):
            if not(words[i] == input[i]):
                False

        return True

    def start(self):

        def nextWord(key):
            keyboard = Controller()
            if key == Key.space:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
        
        lis = Listener(on_press=nextWord)
        lis.start()

        currWord = 0
        mistakes = 0
        correct = 0
        print(self.displayText)
        while currWord < len(self.words):
            userInput = input()
            if(self.compare(self.words[currWord], userInput[:-1])):
                correct += 1
            else:
                mistakes += 1
            currWord += 1
        
        print("Number correct: " + str(correct) + " || Number Wrong: " + str(mistakes))