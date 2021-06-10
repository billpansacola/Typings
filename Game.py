from Words import Words
from tkinter import *

class Game:

    currWord = 0
    mistakes = 0
    correct = 0

    def __init__(self, int):
        self.words = Words().generateWords(int)
        self.displayText = Words().convertListToString(self.words)

    def compare(self, words, input):
        if not(len(words) == len(input)):
            return False
        
        for i in range(0, len(words)):
            if not(words[i] == input[i]):
                return False

        return True

    def start(self):
        root = Tk()
        entry = Entry(root)

        def endGame():
            root.destroy()
            print("Number correct: " + str(self.correct) + " || Number Wrong: " + str(self.mistakes))

        def nextWord(event):
            
            userInput = entry.get()
            entry.delete(0, END)

            if len(userInput) < 2:
                return 0
                
            if self.compare(self.words[self.currWord], userInput[:-1]):
                self.correct += 1
            else:
                self.mistakes += 1
            self.currWord += 1

            if self.currWord == len(self.words):
                endGame()
        
        def redo():
            entry.delete(0,END)
            self.currWord = 0
            self.mistakes = 0
            self.correct = 0
            self.words = Words().generateWords(len(self.words))
            self.displayText = Words().convertListToString(self.words)
            displayText.config(text=self.displayText)

        displayText = Label(root, text=self.displayText)
        redo_button = Button(root, text="Redo", command=redo)

        displayText.grid(row=0, column=0)
        entry.grid(row=1,column=0)
        redo_button.grid(row=1, column=1)
        
        root.bind('<space>', nextWord)
        entry.focus_set()
        root.mainloop()