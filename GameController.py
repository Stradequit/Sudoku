#Sudoku

from tkinter import *

# main:
window = Tk()
window.title("Sudoku")
window.geometry("480x480")
# Puzzle
puzzle = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 5, 5, 5],
          [6, 7, 0, 0, 3, 4, 5, 5, 1],
          []]
# Creating Boxes
boxes = []

for num, val in enumerate(puzzle):
    print()
    if val == 0:
        entry = Entry(width=2).grid(row=num//9 + 1, column=num % 9)
    else:
        label = Label(width=2, text=val).grid(row=num//9 + 1, column=num % 9)
window.mainloop()
