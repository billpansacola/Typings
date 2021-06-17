from Words import Words
from tkinter import *
import math

class Game:

    currWord = 0
    correct = 0
    currIndex = 0

    def __init__(self, int):
        self.words = Words().generateWords(int)
        self.displayText = Words().convertListToString(self.words)

    def compare(self, words, input):
        if not(len(words) == len(input)):
            return False
        else:
            for i in range(0, len(words)):
                if not(words[i] == input[i]):
                    return False

        return True

    def start(self):
        root = Tk()
        entry = Entry(root)
        text = Text(root, width=50, height=5, padx=5, pady=2, wrap=WORD, font="Courier", bg="#F1F1F1")
        text.tag_config("mistake", foreground="red")
        text.tag_config("correct", foreground="green")

        def endGame():
            root.destroy()
            print("Accuracy: " + str(math.floor(self.correct/len(self.words) * 100))+ "%")

        def nextWord(event):
            
            userInput = entry.get()
            entry.delete(0, END)
            if len(userInput) == 1:
                return
            
            text.config(state="normal")
            if self.compare(self.words[self.currWord], userInput[:-1]):
                text.tag_add("correct", "1." + str(self.currIndex), "1." + str(self.currIndex+len(self.words[self.currWord])))
                self.correct += 1
            else:
                text.tag_add("mistake", "1." + str(self.currIndex), "1." + str(self.currIndex+len(self.words[self.currWord])))
            text.config(state="disabled")
            
            self.currIndex += len(self.words[self.currWord]) + 1
            self.currWord += 1

            if self.currWord == len(self.words):
                endGame()
        
        def redo():
            text.config(state="normal")
            entry.delete(0,END)
            self.currWord = 0
            self.correct = 0
            self.currIndex = 0
            self.words = Words().generateWords(len(self.words))
            self.displayText = Words().convertListToString(self.words)
            text.delete(1.0, "end")
            text.insert(INSERT, self.displayText)
            text.config(state="disabled")

        text.insert(INSERT, self.displayText)
        text.config(state="disabled")
        redo_button = Button(root, text="Redo", command=redo)

        text.grid(row=0, column=0)
        entry.grid(row=1,column=0)
        redo_button.grid(row=1, column=1)
        
        root.bind('<space>', nextWord)
        entry.focus_set()
        root.mainloop()